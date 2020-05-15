if (localStorage.getItem('completed') == null) {
	localStorage.setItem('x2', 1);
	localStorage.setItem('y2', 1);
	localStorage.setItem('completed', 0);
	localStorage.setItem('tree', 1);
	localStorage.setItem('x', 0);
	localStorage.setItem('y', 0);
}

x = localStorage.getItem('x');
y = localStorage.getItem('y');
x2 = localStorage.getItem('x2');
y2 = localStorage.getItem('y2');
completed = localStorage.getItem('completed');
tree = localStorage.getItem('tree');
page = 0
checkPos();

function setup() {
	createCanvas(4096, 4096);
}

function draw() {
	// document.getElementById(1).classList.add('stone');
	// document.getElementById(1).classList.remove('grass');
}

function checkPos() {
	if (x2 == 1) {
		x = 17;
	} else if (x2 == 2) {
		x = 80;
	} else if (x2 == 3) {
		x = 143;
	} else if (x2 == 4) {
		x = 206;
	}

	if (y2 == 1) {
		y = 17;
	} else if (y2 == 2) {
		y = 80;
	} else if (y2 == 3) {
		y = 143;
	} else if (y2 == 4) {
		y = 206;
	}

	if (completed == 0) {
		if (tree == 1) {
			if (y2 == 1) {
				if (x2 == 4) {
					asdf = Math.floor(Math.random() * 2);

					if (asdf == 1) {
						y2 = 2;
						x2 = 4;
					} else {
						x2 = 3;
						y2 = 1;
					}
					checkPos();
				}
			}
		}
	}
	localStorage.setItem('x', x);
	localStorage.setItem('y', y);
}

document.addEventListener("keypress", function onEvent(event) {
    if (event.key === "w" | event.key === 'W') {
    	if (y2 != 1) {
	        y2 = parseInt(y2)-1;
	        y2 = y2;
    	}
    }
    else if (event.key === "a" | event.key === 'A') {
        if (x2 != 1) {
        	x2 = parseInt(x2)-1;
        	x2 = x2;
        }
    }
    else if (event.key === 's' | event.key === 'S') {
    	if (y2 != 4) {
    		y2 = parseInt(y2)+1;
    		y2 = y2;
    	}
    }
    else if (event.key === 'd' | event.key === 'D') {
    	if (x2 != 4) {
    		x2 = parseInt(x2)+1;
    		x2 = x2;
    	}
    }
    else if (event.key === 'Enter') {
    	if (y2 == 1) {
    		if (x2 == 3) {
    			tree = 0;
    		}
    	} else if (y2 == 2) {
    		if (x2 == 4) {
    			tree = 0;
    		}
    	} 
    }

    localStorage.setItem('x2', x2);
    localStorage.setItem('y2', y2);
    localStorage.setItem('tree', tree);
    checkPos();
});