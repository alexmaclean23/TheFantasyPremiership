var navigationElements = [];
var contentElements = [];
var scrollNum = 0;

function scrollContent(index) {
    navigationElements = Array.prototype.slice.call(document.querySelectorAll(".uppernav > .navlink:not(:last-of-type)")).concat(Array.prototype.slice.call(document.querySelectorAll(".lowernav > .navlink")));
    contentElements = document.querySelectorAll(".container");
    navigationElements[scrollNum].classList.remove("current");
    contentElements[scrollNum].classList.remove("current");
    if (index == null) {
        console.log("'Null' passed to 'scrollContent'.");
    } else if (index == "-") {
        navigationElements[scrollNum - 1].classList.add("current");
        contentElements[scrollNum - 1].classList.add("current");
        scrollNum--;
    } else if (index == "+") {
        navigationElements[scrollNum + 1].classList.add("current");
        contentElements[scrollNum + 1].classList.add("current");
        scrollNum++;
    } else {
        navigationElements[index].classList.add("current");
        contentElements[index].classList.add("current");
        scrollNum = index;
    }
    expandWrapper("*");
    const scrollID = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];
    const selectID = [0, 2, 4, 7, 45, 69, 14, 17, 20, 81, 26, 29, 32, 33, 35, 105, 108, 42, 44];
    if (scrollID.includes(scrollNum)) {
        selectItem(selectID[scrollID.indexOf(scrollNum)]);
    }
}