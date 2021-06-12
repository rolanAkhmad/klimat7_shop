function toogleMenu(menu_togler, icon1, icon2){
    menu_togler.toggleClass('active')

    if(menu_togler.hasClass('active')){
        menu_togler.html('<span class="material-icons-round lh-1_5">' + icon1 + '</span>')
    }else{
        menu_togler.html('<span class="material-icons-round lh-1_5">' + icon2 + '</span>')
    }
}