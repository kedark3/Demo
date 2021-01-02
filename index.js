const database = ["cat.com", "dog.com","lion.com"];

function googleSearch(searchInput, db) {
  const matches = db.filter(website => { 
    return website.includes(searchInput);
})
  return matches > 3 ? matches.slice(0,3) : matches;
}

const result = googleSearch("cat", database);
console.log(result);
