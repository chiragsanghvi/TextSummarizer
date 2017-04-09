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

var satisfyRequest = function(req, res, language) {

	var experimentId = (language == "Portuguese") ? "155113384972518187" : "155113393118904924";
	var documents = walkSync(__dirname + "/../" + language + "/documents");
	var docsRated = req.cookies['docsRated'];

	if (!docsRated ||  docsRated == "") docsRated = [];
	else docsRated = JSON.parse(docsRated);

	var docName, sumDocName;

	for(var i = 0;i< documents.length; i++) {
		if (docsRated.indexOf(documents[i]) == -1) {
			docName = documents[i];
			sumDocName = docName + "_pageRank";
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
 				res.send("Error fetching summary for document " + docName);
 				return;
 			}

 			res.render('index.ejs', { doc: doc, summary: summary, docName: docName, docsRated: JSON.stringify(docsRated), experimentId: experimentId });
	 	});
 	});
};

app.get('/marathi', (req, res) => {
	satisfyRequest(req, res, 'Marathi');
});

app.get('/portuguese', (req, res) => {
	satisfyRequest(req, res, 'Portuguese');
});

app.get('*', (req, res) => {
	res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(process.env.PORT || 5000, function() {
	console.log('listening on ' + (process.env.PORT || 5000));
})

