var selectionElements = [];
var substanceElements = [];
var selectNum = 0;

function selectItem(index) {
    selectionElements = Array.prototype.slice.call(document.querySelectorAll(".upperselect > .selectlink:not(:last-of-type)")).concat(Array.prototype.slice.call(document.querySelectorAll(".lowerselect > .selectlink")));
    substanceElements = Array.prototype.slice.call(document.querySelectorAll(".item:not(.team):not(.matchup):not(.season)")).concat(Array.prototype.slice.call(document.querySelectorAll(".item:not(.payment):not(.transfers):not(.view):not(.download):not(.division):not(.complete):not(.scores):not(.configure)")));
    selectionElements[selectNum].classList.remove("current");
    substanceElements[selectNum].classList.remove("current");
    if (index == null) {
        console.log("'Null' passed to 'selectItem'.");
    } else {
        selectionElements[index].classList.add("current");
        substanceElements[index].classList.add("current");
        selectNum = index;
    }
}