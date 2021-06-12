$('.list-view ').on('click', function(){
    $('.store-product-list').toggleClass('store-product-list_list-view')
    $('.card').toggleClass('card_list-view')
})

$('.grid-view').on('click', function(){
    $('.store-product-list').removeClass('store-product-list_list-view')
    $('.card').removeClass('card_list-view')
})


