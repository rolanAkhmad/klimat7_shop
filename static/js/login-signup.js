new Glide('#gas_boiler_slider',{
    type: 'slider',
    startAt: 0,
    perView: 3,
    gap: 20,
    breakpoints: {
        600: { perView: 1 },
        1200: { perView: 3 }
    },
    bound: true,
}).mount()

new Glide('#gas_gorel_slider',{
    type: 'slider',
    startAt: 0,
    perView: 3,
    gap: 20,
    breakpoints: {
        600: { perView: 1 },
        1200: { perView: 3 }
    },
    bound: true
}).mount()