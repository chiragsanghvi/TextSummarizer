const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const fs = require('fs');
const path = require('path');
const Appacitive = require('appacitive')

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));
app.use(cookieParser());

Appacitive.initialize({ 
  apikey: "rPntDlXHGtzYQ2JEot+Bxit14lW9A/Qw7+BrTJ5bPdo=",// The master or client api key for your app on appacitive.
  env: "sandbox",      // The environment that you are targetting (sandbox or live).
  appId: "155028085042971632"     // The app id for your app on appacitive. 
});
var Experiment = Appacitive.Object.extend('experiment');

// List all files in a directory in Node.js recursively in a synchronous fashion
var walkSync = function(dir) {
  var path = path || require('path');
  var fs = fs || require('fs'),
      files = fs.readdirSync(dir);

  var filelist = [];
  files.forEach(function(file) {
    if (fs.statSync(path.join(dir, file)).isDirectory()) {
      filelist = walkSync(path.join(dir, file), filelist);
    }
    else {
      filelist.push(file);
    }
  });
  return filelist;
};

var experimentIds = {
	"Portuguese" : {
		"TextRankSummarizer" : "155113384972518187",
		"LexRankSummarizer" : "155124091687404194",
		"LsaSummarizer" : "155124106131538600",
		"LuhnSummarizer" : "155124114800116696",
		"SumBasicSummarizer" : "155124125727327204",
		"Human": "155177166949188379"
	},
	"Marathi" : {
		"PageRankSummarizer": "155113393118904924",
		"Human": "155177156937384892"
	}
}

var satisfyRequest = function(req, res, language) {

	var documents = walkSync(__dirname + "/../" + language + "/summaries");
	var docsRated = req.cookies['docsRated'];

	if (!docsRated ||  docsRated == "") docsRated = [];
	else docsRated = JSON.parse(docsRated);

	var docName, sumDocName;

	for(var i = 0;i< documents.length; i++) {
		if (docsRated.indexOf(documents[i]) == -1) {
			sumDocName = documents[i];
			var split = sumDocName.split('_');
			algorithm = split[split.length - 1];
			docName = sumDocName.replace("_" + algorithm, "");
			break;
		}	
	}

	if (!docName) {
		res.send("No more documents to rate. Come back later");
		return;
	}

	var experimentId = experimentIds[language][algorithm];
	
 	fs.readFile(__dirname + "/../"  + language + '/summaries/' + sumDocName, 'utf-8', function(err, summary) {
 		if (err) {
			res.send("Error fetching summary for  document " + sumDocName + "\n" + err.message);
			return;
		}
 		fs.readFile(__dirname + "/../" + language + '/documents/' + docName, 'utf-8', function(err, doc) {
 			if (err) {
 				res.send("Error fetching document " + docName + "\n" + err.message);
 				return;
 			}

 			res.render('index.ejs', { 
 				doc: doc, 
 				summary: summary, 
 				docName: docName, 
 				sumDocName: sumDocName,
 				docsRated: JSON.stringify(docsRated), 
 				experimentId: experimentId, 
 				algorithm: algorithm, 
 				language: language
 			});
	 	});
 	});
};

app.get('/marathi', (req, res) => {
	satisfyRequest(req, res, 'Marathi');
});

app.get('/portuguese', (req, res) => {
	satisfyRequest(req, res, 'Portuguese');
});

app.get('/results', (req,res) => {
	Experiment.findAll({ fields: ["*"] }).fetch().then(function(exps) {
		var langs = {};

		exps.forEach(function(exp) {
			var expJ = exp.toJSON();
			if (!langs[expJ.language]) langs[expJ.language] = [];

			if (expJ['$average']) expJ.average = expJ['$average'].all || 0;
			else expJ.average = 0;

			if (expJ['$count']) expJ.count = expJ['$count'].all || 0;
			else expJ.count = 0;

			if (expJ['$max']) expJ.max = expJ['$max'].all || 0;
			else expJ.max = 0;

			if (expJ['$min']) expJ.min = expJ['$min'].all || 0;
			else expJ.min = 0;

			langs[expJ.language].push(expJ);
		});

		//res.send(JSON.stringify(langs));

		res.render('results.ejs', { langs: langs });
	}, function(err) {
		res.send("Error fetching results " + err.message);
	});
});

app.get('*', (req, res) => {
	res.sendFile('index.html', {"root": __dirname});
});

app.use(function(req, res){
   res.sendFile('index.html', {"root": __dirname});
});

app.listen(process.env.PORT || 5000, function() {
	console.log('listening on ' + (process.env.PORT || 5000));
})

