function expandWrapper(index) {
    wrapperElements = Array.prototype.slice.call(document.querySelectorAll(".wrapper"));
    resizeElements = Array.prototype.slice.call(document.querySelectorAll(".resize i"));
    if (index === "*") {
        for (index = 0; index < wrapperElements.length; index++) {
            wrapperElements[index].classList.remove("zoomed");
            resizeElements[index].classList.remove("fa-compress");
            resizeElements[index].classList.add("fa-expand");
        }
    } else {
        if (wrapperElements[index].classList.contains("zoomed")) {
            wrapperElements[index].classList.remove("zoomed");
            resizeElements[index].classList.remove("fa-compress");
            resizeElements[index].classList.add("fa-expand");
        } else {
            wrapperElements[index].classList.add("zoomed");
            resizeElements[index].classList.remove("fa-expand");
            resizeElements[index].classList.add("fa-compress");
        }
    }
}