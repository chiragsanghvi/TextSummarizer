const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const fs = require('fs');
const path = require('path');
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));
app.use(cookieParser());

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
		"SumBasicSummarizer" : "155124125727327204"
	},
	"Marathi" : {
		"PageRankSummarizer": "155113393118904924"
	}
}

var satisfyRequest = function(req, res, language, algorithm) {

	var experimentId = experimentIds[language][algorithm];

	var documents = walkSync(__dirname + "/../" + language + "/documents");
	var docsRated = req.cookies['docsRated'];

	if (!docsRated ||  docsRated == "") docsRated = [];
	else docsRated = JSON.parse(docsRated);

	var docName, sumDocName;

	for(var i = 0;i< documents.length; i++) {
		if (docsRated.indexOf(documents[i]) == -1) {
			docName = documents[i];
			sumDocName = docName + "_" + algorithm;
			break;
		}	
	}

	if (!docName) {
		res.send("No more documents to rate. Come back later");
		return;
	}

 	fs.readFile(__dirname + "/../"  + language + '/documents/' + docName, 'utf-8', function(err, doc) {
 		if (err) {
			res.send("Error fetching document " + docName);
			return;
		}
 		fs.readFile(__dirname + "/../" + language + '/summaries/' + sumDocName, 'utf-8', function(err, summary) {
 			if (err) {
 				res.send("Error fetching summary for document " + sumDocName);
 				return;
 			}

 			res.render('index.ejs', { doc: doc, summary: summary, docName: docName, docsRated: JSON.stringify(docsRated), experimentId: experimentId, algorithm: algorithm, language: language });
	 	});
 	});
};

app.get('/marathi', (req, res) => {
	satisfyRequest(req, res, 'Marathi', 'PageRankSummarizer');
});



app.get('/Portuguese/LexRankSummarizer', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'LexRankSummarizer');
});

app.get('/Portuguese/LuhnSummarizer', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'LuhnSummarizer');
});

app.get('/Portuguese/LsaSummarizer', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'LsaSummarizer');
});

app.get('/Portuguese/SumBasicSummarizer', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'SumBasicSummarizer');
});

app.get('/Portuguese/TextRankSummarizer', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'TextRankSummarizer');
});

app.get('/Portuguese', (req, res) => {
	satisfyRequest(req, res, 'Portuguese', 'TextRankSummarizer');
});

app.get('*', (req, res) => {
	res.sendFile(path.join(__dirname + '/index.html'));
});

app.use(function(req, res){
   res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(process.env.PORT || 5000, function() {
	console.log('listening on ' + (process.env.PORT || 5000));
})

