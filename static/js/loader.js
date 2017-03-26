/**
 * Created by hou on 16-12-11.
 */
$(document).ready(function () {
   $('.ui.accordion').accordion('close');//
   $('.ui.dropdown').dropdown();
   $('.ui.sidebar').sidebar({
      dimPage: false,closable:false
   });
});

// function changesidebar() {
//    var changecss=document.getElementById("thinsidebar");
//
//    if(changecss.getAttribute("class").search("very thin")){
//       changecss.setAttribute("class","ui visible inverted left thin vertical sidebar menu");
//    }
//    else {
//       changecss.setAttribute("class","ui visible inverted left very thin vertical sidebar menu");
//    }
//
//
// }
