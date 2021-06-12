new Glide('#banner_slider',{
    type: 'slider',
    startAt: 0,
    perView: 1,
    gap: 20,
    bound: true,
}).mount()

new Glide('#new-arriwal-slider',{
    type: 'slider',
    startAt: 0,
    perView: 2,
    gap: 20,
    bound: true,
    breakpoints: {
        600: { perView: 1 },
        1200: { perView: 1 }
    },
}).mount()

new Glide('#new-arriwal-slider',{
    type: 'carousel',
    startAt: 0,
    perView: 2,
    gap: 10,
    peek:{ before: 0, after: 50 },
    breakpoints: {
        600: { perView: 1 },
        1200: { perView: 1 }
    },
}).mount()


new Glide('#top-slider',{
    type: 'carousel',
    startAt: 0,
    perView: 2,
    gap: 10,
    peek:{ before: 0, after: 50 },
    breakpoints: {
        600: { perView: 1 },
        1200: { perView: 1 }
    },
}).mount()


new Glide('#gas_boilers_slider',{
    type: 'carousel',
    startAt: 0,
    perView: 4,
    gap: 10,
    peek:{ before: 0, after: 50 },
    breakpoints:{
        1120:{
            perView: 3
        },
        960:{
            perView: 2
        },
        620:{
            perView: 1
        }
    }
}).mount()

new Glide('#gas_gorel_slider',{
    type: 'carousel',
    startAt: 0,
    perView: 4,
    gap: 10,
    peek:{ before: 0, after: 50 },
    breakpoints:{
        1120:{
            perView: 3
        },
        960:{
            perView: 2
        },
        620:{
            perView: 1
        }
    }
}).mount()
