#!/usr/bin/node

const program = require('commander');
const axios = require('axios').default;

function correctCommands(options) {
    if (options.format != undefined) {
        if (options.format == "csv" || options.format == "json")
            return true
        else {
            console.log('Supported formats are "json" and "csv" only')
            return false
        }
    }
    if (options.datefrom == undefined && options.dateto != undefined) {
        console.log('Can\'t have "to" without "from"')
        return false
    }
    return true
}


//commands
//SessionsPerPoint
program
    .command('SessionsPerPoint')
    .option('--point <point_id>', 'from point')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .option('--format <format>', 'data in json or csv')
    .action(function(options) {

        if (options.point == undefined) {
            console.log("Must define point using '--point' option")
            return
        }
        if (!correctCommands(options)) return

        let config = {
            method: 'get',
            url: 'http://localhost:8765/evcharge/api/SessionsPerPoint/' +
                ((options.point != undefined) ? options.point : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : '') +
                ((options.format != undefined) ? '?format=' + options.format : '')
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })

//SessionsPerStation
program
    .command('SessionsPerStation')
    .option('--station <station_id>', 'from station')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .option('--format <format>', 'data in json or csv')
    .action(function(options) {

        if (options.station == undefined) {
            console.log("Must define station using '--station' option")
            return
        }
        if (!correctCommands(options)) return

        let config = {
            method: 'get',
            url: 'http://localhost:8765/evcharge/api/SessionsPerStation/' +
                ((options.station != undefined) ? options.station : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : '') +
                ((options.format != undefined) ? '?format=' + options.format : '')
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })

//SessionsPerEV
program
    .command('SessionsPerEV')
    .option('--ev <vehicle_id>', 'for electric vehicle')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .option('--format <format>', 'data in json or csv')
    .action(function(options) {

        if (options.ev == undefined) {
            console.log("Must define ev using '--ev' option")
            return
        }
        if (!correctCommands(options)) return

        let config = {
            method: 'get',
            url: 'http://localhost:8765/evcharge/api/SessionsPerEV/' +
                ((options.ev != undefined) ? options.ev : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : '') +
                ((options.format != undefined) ? '?format=' + options.format : '')
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })

//SessionsPerProvider
program
    .command('SessionsPerProvider')
    .option('--provider <provider_id>', 'for provider')
    .option('--datefrom <startdate>', 'from start date')
    .option('--dateto <finishdate>', 'to finish date')
    .option('--format <format>', 'data in json or csv')
    .action(function(options) {

        if (options.provider == undefined) {
            console.log("Must define provider using '--provider' option")
            return
        }
        if (!correctCommands(options)) return


        let config = {
            method: 'get',
            url: 'http://localhost:8765/evcharge/api/SessionsPerProvider/' +
                ((options.provider != undefined) ? options.provider : '') +
                ((options.datefrom != undefined) ? '/' + options.datefrom : '') +
                ((options.dateto != undefined) ? '/' + options.dateto : '') +
                ((options.format != undefined) ? '?format=' + options.format : '')
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })

//healthcheck
program
    .command('healthcheck')
    .action(function() {

        let config = {
            method: 'get',
            url: 'http://localhost:8765/evcharge/api/admin/healthcheck'
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })


//login
program
    .command('login')
    .option('--username <username>', 'given username to attempt login')
    .option('--passw <password>', 'given password to attempt login')
    .action(function(options) {

        if (options.username == undefined) {
            console.log("Option '--username' must be given")
            return
        }
        if (options.passw == undefined) {
            console.log("Option '--passw' must be given")
            return
        }

        let config = {
            method: 'post',
            url: 'http://localhost:8765/evcharge/api/login',
            data: {
                username: options.username,
                password: options.passw
            }
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })


//logout
program
    .command('logout')
    .action(function() {

        let config = {
            method: 'post',
            url: 'http://localhost:8765/evcharge/api/logout'
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })


// resetsessions
program
    .command('resetsessions')
    .action(function() {

        let config = {
            method: 'post',
            url: 'http://localhost:8765/admin/resetsessions/'
        }
        axios(config)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log("Status code: " + err.response.status)
                if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                    console.log(err.response.data)
                if (err.response.status == 404)
                    console.log("Page Not Found")
            })
    })



// Admin
program
    .command('Admin')
    .option('--usermod', 'modify user or add new user')
    .option('--username <username>', 'given username to create or update password of')
    .option('--passw <password>', 'given password to modify')
    .option('--users <username>', 'check whether given user is logged in')
    .option('--sessionsupd', 'give csv file to create new sessions')
    .option('--source <filename>', 'source file for --sessionsupd')
    .option('--healthcheck', 'check connection with db')
    .option('--resetsessions', 'delete all charging sessions and initialize admin')
    .action(function(options) {

        if (options.usermod != undefined) {

            if (options.username == undefined) {
                console.log("Option '--username' must be given")
                return
            }
            if (options.passw == undefined) {
                console.log("Option '--passw' must be given")
                return
            }

            let config = {
                method: 'post',
                url: 'http://localhost:8765/evcharge/api/admin/usermod/' + options.username + '/' + options.passw
            }
            axios(config)
                .then(res => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log("Status code: " + err.response.status)
                    if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                        console.log(err.response.data)
                    if (err.response.status == 404)
                        console.log("Page Not Found")
                })
            return
        }

        if (options.users != undefined) {
            let config = {
                method: 'get',
                url: 'http://localhost:8765/evcharge/api/admin/users/' + options.users
            }
            axios(config)
                .then(res => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log("Status code: " + err.response.status)
                    if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                        console.log(err.response.data)
                    if (err.response.status == 404)
                        console.log("Page Not Found")
                })
            return
        }

        if (options.sessionsupd) {

            console.log("Option '--sessionsupd' currently unavailable")
            return

            // if (options.source == undefined) {
            //     console.log("Option '--source' must be given")
            //     return
            // }

            // const fs = require('fs')
            // var FormData = require('form-data')
            // let formdata = new FormData()
            // formdata.append('file', fs.createReadStream('./' + options.source))
            // console.log(formdata)
            // let config = {
            //     method: 'post',
            //     url: 'http://localhost:8765/evcharge/api/admin/system/sessionsupd',
            //     headers: {
            //         'Content-Type': 'multipart/form-data'
            //     },
            //     data: {
            //         "file": formdata
            //     }
            // }

            // axios.request(config)
            //     .then(res => {
            //         console.log(res.data)
            //     })
            //     .catch(err => {
            //         console.log("Status code: " + err)
            //             // console.log(err)
            //     })

            // return
        }

        if (options.healthcheck) {
            let config = {
                method: 'get',
                url: 'http://localhost:8765/evcharge/api/admin/healthcheck'
            }
            axios(config)
                .then(res => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log("Status code: " + err.response.status)
                    if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                        console.log(err.response.data)
                    if (err.response.status == 404)
                        console.log("Page Not Found")
                })
            return
        }

        if (options.resetsessions) {
            let config = {
                method: 'post',
                url: 'http://localhost:8765/evcharge/api/admin/resetsessions'
            }
            axios(config)
                .then(res => {
                    console.log(res.data)
                })
                .catch(err => {
                    console.log("Status code: " + err.response.status)
                    if (err.response.status == 400 || err.response.status == 401 || err.response.status == 402)
                        console.log(err.response.data)
                    if (err.response.status == 404)
                        console.log("Page Not Found")
                })
            return
        }



    })





program.parse(process.argv);