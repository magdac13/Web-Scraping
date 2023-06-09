fetch("https://occ-0-3911-1433.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABcihUr0p7lptnWRV3Ygxqzy9ujzUQtzWvSR3CZ_AsbljexMbNRvr9CVgrwotVYhMz20IpUSLLAaPg76AN-Qll6KBvSCE2cvMEtc24kjk3SAfEkCqmwgQqtm8lY6y4p9I0cpAqA.jpg?r=ad1")
    .then(res => res.json())
    .then(res => {
        console.log(res);
        //const war = res.find(el => el.stacja === "Warszawa");
        //console.log(war)
    })
