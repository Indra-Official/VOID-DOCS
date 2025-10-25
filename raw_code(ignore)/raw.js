function side_slide(){
    document.getElementById("how").addEventListener("click", function(){this.textContent = ">>"})
    document.getElementById("side").classList.toggle("active")
    
}