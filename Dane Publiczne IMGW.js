fetch("https://danepubliczne.imgw.pl/api/data/synop")
    .then(res => res.json())
    .then(res => {
        console.log(res);
        const war = res.find(el => el.stacja === "Warszawa");
        console.log(war)
    })
