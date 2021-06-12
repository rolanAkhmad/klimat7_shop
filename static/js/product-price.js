document.querySelectorAll('.product_price').forEach(function(el) {
    price = parseFloat(el.textContent);
    result = price.toLocaleString()
    result += ' ₸'
    el.textContent = result
});