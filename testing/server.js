var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
require("date-format-lite");
// var MongoClient = require('mongodb').MongoClient;
var mongoose = require('mongoose');

var port = 8080;
var app = express();

const url = ''

mongoose.connect(url);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function callback() {
    console.log("h");
});

const router = express.Router();
const Schema = mongoose.Schema;;

let productSchema = new Schema({
    task_id: { type: String },
    task_name: { type: String }
}, { collection: 'sample' });

const Product = mongoose.model('Product', productSchema);

// Create get request to get all products from database
router.get('/', function(req, res, next) {
    // Get all products in the database
    Product.find({}, function(err, data) {
        if (err) {
            throw err;
        }
        // res.render('index', { products: data });
        // Send the data to the webpage
        console.log(data);
        res.json(data);
    });
});

router.use('/chart', express.static(path.join(__dirname, "public")));

module.exports = router;

// app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({ extended: true }));

app.use(router);

app.listen(port, function() {
    console.log("Server is running on port " + port + "...");
});