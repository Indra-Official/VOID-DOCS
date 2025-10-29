// Get form elements
const passwordInput = document.getElementById('password');
const submitButton = document.querySelector('button[type="submit"]');
const form = document.querySelector('form');

// Disable submit button initially
submitButton.disabled = true;
submitButton.style.opacity = '0.5';
submitButton.style.cursor = 'not-allowed';
submitButton.style.pointerEvents = 'none'; // prevents clicking

// Create overlay container for alerts
const alertContainer = document.createElement('div');
alertContainer.id = 'security-alert-container';
alertContainer.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    width: 280px;
    max-height: 90vh;
    overflow-y: auto;
    z-index: 10000;
    pointer-events: none;
`;
document.body.appendChild(alertContainer);

// Add CSS animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    #security-alert-container::-webkit-scrollbar {
        width: 6px;
    }
    #security-alert-container::-webkit-scrollbar-track {
        background: transparent;
    }
    #security-alert-container::-webkit-scrollbar-thumb {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 3px;
    }
`;
document.head.appendChild(style);

// Password validation rules
const validationRules = {
    minLength: {
        test: (password) => password.length >= 8,
        message: 'At least 8 characters'
    },
    hasUpperCase: {
        test: (password) => /[A-Z]/.test(password),
        message: 'One uppercase letter'
    },
    hasLowerCase: {
        test: (password) => /[a-z]/.test(password),
        message: 'One lowercase letter'
    },
    hasNumber: {
        test: (password) => /[0-9]/.test(password),
        message: 'At least one number'
    },
    hasSpecialChar: {
        test: (password) => /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password),
        message: 'One special character'
    }
};

// Debounce timer for typing delay
let typingTimer;
const typingDelay = 500; // 500ms delay after user stops typing

// Function to create alert tab (only for failed validations)
function createAlertTab(id, message) {
    const tab = document.createElement('div');
    tab.id = `alert-${id}`;
    tab.style.cssText = `
        background: #000000;
        color: #ffffff;
        padding: 8px 12px; /* smaller */
        margin-bottom: 4px; /* smaller spacing */
        border-radius: 4px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13px; /* smaller text */
        font-weight: 500;
        animation: slideIn 0.3s ease-out;
        pointer-events: auto;
        transition: all 0.3s ease;
        border: 1.5px solid #ff0000;
    `;

    const messageSpan = document.createElement('span');
    messageSpan.style.cssText = `flex: 1;`;
    messageSpan.textContent = message;

    const statusIcon = document.createElement('span');
    statusIcon.style.cssText = `
        font-size: 16px;
        font-weight: bold;
        flex-shrink: 0;
        margin-left: 8px;
        color: #ff0000;
    `;
    statusIcon.textContent = '✗';

    tab.appendChild(messageSpan);
    tab.appendChild(statusIcon);
    return tab;
}

// Function to validate password
function validatePassword(password) {
    const results = {};
    let allPassed = true;

    for (const [key, rule] of Object.entries(validationRules)) {
        results[key] = rule.test(password);
        if (!results[key]) allPassed = false;
    }

    return { results, allPassed };
}

// Function to update alert overlay (only show failed validations)
function updateAlertOverlay(validation) {
    alertContainer.innerHTML = '';

    // Count failed validations
    const failedCount = Object.values(validation.results).filter(result => !result).length;

    // Add header only if there are failed validations
    if (!validation.allPassed) {
        const header = document.createElement('div');
        header.style.cssText = `
            background: #000000;
            color: #ffffff;
            padding: 10px 12px;
            margin-bottom: 6px;
            border-radius: 4px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 14px;
            font-weight: 600;
            animation: slideIn 0.3s ease-out;
            pointer-events: auto;
            text-align: center;
            border: 1.5px solid #ff0000;
        `;
        header.textContent = `${failedCount} Requirement${failedCount > 1 ? 's' : ''} Not Met`;
        alertContainer.appendChild(header);

        for (const [key, rule] of Object.entries(validationRules)) {
            if (!validation.results[key]) {
                const tab = createAlertTab(key, rule.message);
                alertContainer.appendChild(tab);
            }
        }

        // Disable button
        submitButton.disabled = true;
        submitButton.style.opacity = '0.5';
        submitButton.style.cursor = 'not-allowed';
        submitButton.style.pointerEvents = 'none';
    } else {
        alertContainer.innerHTML = '';
        // Enable button
        submitButton.disabled = false;
        submitButton.style.opacity = '1';
        submitButton.style.cursor = 'pointer';
        submitButton.style.pointerEvents = 'auto';
    }
}

// Listen for password input with debounce delay
passwordInput.addEventListener('input', function () {
    const password = this.value;

    clearTimeout(typingTimer);

    if (password.length === 0) {
        alertContainer.innerHTML = '';
        submitButton.disabled = true;
        submitButton.style.opacity = '0.5';
        submitButton.style.cursor = 'not-allowed';
        submitButton.style.pointerEvents = 'none';
        return;
    }

    typingTimer = setTimeout(() => {
        const validation = validatePassword(password);
        updateAlertOverlay(validation);
    }, typingDelay);
});

// Validate immediately on blur
passwordInput.addEventListener('blur', function () {
    const password = this.value;
    if (password.length > 0) {
        clearTimeout(typingTimer);
        const validation = validatePassword(password);
        updateAlertOverlay(validation);
    }
});

// Prevent form submission if validation fails
form.addEventListener('submit', function (e) {
    const password = passwordInput.value;
    const validation = validatePassword(password);

    if (!validation.allPassed) {
        e.preventDefault();

        const blockOverlay = document.createElement('div');
        blockOverlay.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: #000000;
            color: #ffffff;
            padding: 30px 40px;
            border-radius: 4px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
            z-index: 10001;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            text-align: center;
            animation: slideIn 0.3s ease-out;
            border: 2px solid #ff0000;
        `;

        blockOverlay.innerHTML = `
            <div style="font-size: 48px; margin-bottom: 16px; color: #ff0000;">✗</div>
            <div style="font-size: 18px; font-weight: 600; margin-bottom: 10px;">Security Requirements Not Met</div>
            <div style="font-size: 14px; opacity: 0.9;">Please complete all password requirements</div>
            <button style="margin-top: 20px; padding: 10px 24px; background: #ffffff; color: #000000; border: 2px solid #000000; border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 14px;">OK</button>
        `;

        const okButton = blockOverlay.querySelector('button');
        okButton.addEventListener('click', () => blockOverlay.remove());

        document.body.appendChild(blockOverlay);
    }
});
