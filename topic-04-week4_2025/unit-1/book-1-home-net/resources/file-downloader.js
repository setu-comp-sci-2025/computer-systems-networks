const fs = require('fs')
const request = require('request')
const progress = require('request-progress')

progress(request('https://goo.gl/pXKZuV'))
 .on('progress', state => {
   console.log(state)
  })
  .on('error', err => console.log(err))
  .on('end', () => {})
  .pipe(fs.createWriteStream('bar.zip'))