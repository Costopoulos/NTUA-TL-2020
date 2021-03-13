const program = require('commander');
const axios = require('axios').default;

//commands
//SessionsPerPoint
program
    .command('SessionsPerPoint')
    .option('--point <point_id>', 'from point')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .action(function(options) {
        if (options.datefrom == undefined && options.dateto != undefined) {
            console.log('Can\'t have "to" without "from"')
            return
        }
        if (options.point == undefined && (options.datefrom != undefined || options.dateto != undefineds)) {
            console.log('Can\'t have dates without --point')
            return
        }
        axios.get('http://localhost:8765/SessionsPerPoint/' +
                ((options.point != undefined) ? options.point : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : ''))
            .then(function(response) {
                console.log(response.data)
            })
    })

//SessionsPerStation
program
    .command('SessionsPerStation')
    .option('--station <station_id>', 'from station')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .action(function(options) {
        if (options.datefrom == undefined && options.dateto != undefined) {
            console.log('Can\'t have "to" without "from"')
            return
        }
        if (options.station == undefined && (options.datefrom != undefined || options.dateto != undefineds)) {
            console.log('Can\'t have dates without --station')
            return
        }
        axios.get('http://localhost:8765/SessionsPerStation/' +
                ((options.station != undefined) ? options.station : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : ''))
            .then(function(response) {
                console.log(response.data)
            })
    })

//SessionsPerEV
program
    .command('SessionsPerEV')
    .option('--ev <vehicle_id>', 'for electric vehicle')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .action(function(options) {
        if (options.datefrom == undefined && options.dateto != undefined) {
            console.log('Can\'t have "to" without "from"')
            return
        }
        if (options.ev == undefined && (options.datefrom != undefined || options.dateto != undefineds)) {
            console.log('Can\'t have dates without --ev')
            return
        }
        axios.get('http://localhost:8765/SessionsPerEV/' +
                ((options.ev != undefined) ? options.ev : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : ''))
            .then(function(response) {
                console.log(response.data)
            })
    })

//SessionsPerProvider
program
    .command('SessionsPerProvider')
    .option('--provider <provider_id>', 'for provider')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .action(function(options) {
        if (options.datefrom == undefined && options.dateto != undefined) {
            console.log('Can\'t have "to" without "from"')
            return
        }
        if (options.provider == undefined && (options.datefrom != undefined || options.dateto != undefineds)) {
            console.log('Can\'t have dates without --provider')
            return
        }
        let config = {
            method: 'get',
            url: 'http://localhost:8765/SessionsPerProvider/' +
            ((options.provider != undefined) ? options.provider : '') +
            ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
            ((options.dateto != undefined) ? '/' + options.dateto : ''),
            
        }
        axios(config)
        .then(res => {
            console.log(res.data)
        })
        .catch(err => {
            console.log(err)
        })
        // axios.get('http://localhost:8765/SessionsPerProvider/' +
        //         ((options.provider != undefined) ? options.provider : '') +
        //         ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
        //         ((options.dateto != undefined) ? '/' + options.dateto : ''))
        //     .then(function(response) {
        //         console.log(response.data)
        //     })
    })

program.parse(process.argv);