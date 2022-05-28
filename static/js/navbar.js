const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const searchBtn = document.querySelector(".searchbutton")


hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
})


document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", ()=>{
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}))

document.querySelectorAll(".searchbutton").forEach(n => n.addEventListener("click", ()=>{
    searchBtn.classList.remove("active")
}))