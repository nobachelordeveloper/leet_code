//Press F8 or highlight and press F8 to run javascript code

var bool = false;
// var scope = "before while";
while(bool) {
	var scope = "detected"
	var randInt = Math.floor(Math.random()*10);
	if (randInt === 5) {
		bool = true
	}
}
console.log(scope)
