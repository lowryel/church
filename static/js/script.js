const faders = document.querySelectorAll(".fade-in");

const appearOptions = {
    threshold: 1,
    rootMargin: "0px 0px -50px 0px"
};

const appearOnScroll = new IntersectionObserver((entries, appearOnScroll)=>{
    entries.forEach(entry => {
        if (!entry.isIntersecting){
            return;
        }else
        {
            entry.target.classList.add("appear");
            appearOnScroll.unobserve(entry.target);
        }
    })
}, appearOptions)

faders.forEach(fader => {
    appearOnScroll.observe(fader);
})


// show slide in on mobile view
// const appearOnScrollInMobileView = new IntersectionObserver((entries, appearOnScrollInMobileView) => {
//   entries.forEach((entry) => {
//     if (!entry.isIntersecting) {
//       return;
//     } else {
//       entry.target.classList.add("show");
//       appearOnScrollInMobileView.unobserve(entry.target);
//     }
//   });
// }, appearOptions);

// faders.forEach((fader) => {
//   appearOnScrollInMobileView.observe(fader);
// });

