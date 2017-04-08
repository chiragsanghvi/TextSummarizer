const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const fs = require('fs');

app.set('view engine', 'ejs');
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

app.get('/', (req, res) => {

	var documents = walkSync(__dirname + "/documents");
	var docsRated = req.cookies['docsRated'];

	if (!docsRated ||  docsRated == "") docsRated = [];

	var docName, sumDocName;

	for(var i = 0;i< documents.length; i++) {
		if (docsRated.indexOf(documents[i]) == -1) {
			docName = documents[i];
			sumDocName = docName.replace(".txt", "_pageRank.txt");
			break;
		}	
	}

	if (!docName) {
		res.send("No more documents to rate. Come back later");
		return;
	}

 	fs.readFile('documents/' + docName, 'utf-8', function(err, doc) {
 		if (err) {
			res.send("Error fetching document " + docName);
			return;
		}
 		fs.readFile('summaries/' + sumDocName, 'utf-8', function(err, summary) {
 			if (err) {
 				res.send("Error fetching summary for document " + docName);
 				return;
 			}

 			res.render('index.ejs', { doc: doc, summary: summary, docName: docName, docsRated: JSON.stringify(docsRated) });
	 	});
 	});
});

app.listen(process.env.PORT || 3000, function() {
	console.log('listening on 3000')
})

