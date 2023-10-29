// Get references to the relevant HTML elements
const labelEl = document.getElementById('label');
const dateEl = document.getElementById('date');
const agentsEl = document.getElementById('agents');
const imageEl = document.getElementById('image');

// Add an event listener to the "Next" button
const nextBtn = document.getElementById('next-btn');
nextBtn.addEventListener('click', getNextObject);

// Add an event listener to the "Pause" button
const pauseBtn = document.getElementById('pause-btn');
pauseBtn.addEventListener('click', togglePause);

// Set the timer interval to 5 seconds
let intervalId = setInterval(getNextObject, 5000);

let objectIds = [];

// Function to retrieve information about the next random object
function getNextObject() {
  // Check if objectIds array is empty
  if (objectIds.length === 0) {
    // Extract the object ID from the image src
    const objectId = document.getElementById('object-id').value;
    // Add the object ID to the objectIds array
    objectIds.push(objectId);
    console.log("id:", objectId)
  }
  // Send an AJAX request to the /next_object route
  fetch('/next_object')
    .then(response => response.json())
    .then(data => {
      // Update the HTML elements with the new object details
      labelEl.textContent = data.label;
      dateEl.textContent = data.date;
      // Clear the existing list of agents
      agentsEl.innerHTML = '';

      // Create a list item for each agent
      for (const agent of data.agents) {
        const agentItem = document.createElement('li');
        agentItem.textContent = agent;
        agentsEl.appendChild(agentItem);
      }

      imageEl.src = `https://media.collections.yale.edu/thumbnail/yuag/obj/${data.object_id}`;
      imageEl.alt = `${data.label}, ${data.date}`;

      // Add an error handler to handle image loading errors
      imageEl.onerror = () => {
        imageEl.src = '/static/image_not_available.png';
        imageEl.alt = 'Image not available';
      };
      // Add the current object ID to the array
      objectIds.push(data.object_id);
      console.log("ids:", objectIds)
    })
    .catch(error => console.error(error));
}

// Function to toggle the pause/resume state
function togglePause() {
  if (pauseBtn.textContent === 'Pause') {
    clearInterval(intervalId);
    pauseBtn.textContent = 'Resume';
  } else {
    getNextObject();
    intervalId = setInterval(getNextObject, 5000);
    pauseBtn.textContent = 'Pause';
  }
}


// Get a reference to the "Previous" button
const prevBtn = document.getElementById('prev-btn');

// Add an event listener to the "Previous" button
prevBtn.addEventListener('click', handlePrevClick);

// Function to retrieve information about the previous object
function getPrevObject() {
    // Remove the most recent ID from the array
    objectIds.pop();
    console.log("ids:", objectIds)

    if (objectIds.length <= 0) {
      alert('There are no previous objects.');
      return;
    }

    // Get the ID of the previous object
    const prevObjectId = objectIds[objectIds.length - 1];

    // Send an AJAX request to the /prev_object/<int:obj_id> route
    fetch(`/prev_object/${prevObjectId}`)
      .then(response => response.json())
      .then(data => {
        // Update the HTML elements with the new object details
        labelEl.textContent = data.label;
        dateEl.textContent = data.date;
        // Clear the existing list of agents
        agentsEl.innerHTML = '';

        // Create a list item for each agent
        for (const agent of data.agents) {
          const agentItem = document.createElement('li');
          agentItem.textContent = agent;
          agentsEl.appendChild(agentItem);
        }

        imageEl.src = `https://media.collections.yale.edu/thumbnail/yuag/obj/${data.object_id}`;
        imageEl.alt = `${data.label}, ${data.date}`;

        // Add an error handler to handle image loading errors
        imageEl.onerror = () => {
          imageEl.src = '/static/image_not_available.png';
          imageEl.alt = 'Image not available';
        };
      })
      .catch(error => console.error(error));
  }


// Function to handle clicks on the "Previous" button
function handlePrevClick() {
  // Stop the automatic retrieval of object information
  clearInterval(intervalId);
  pauseBtn.textContent = 'Resume';

  // Retrieve information about the previous object
  getPrevObject();
}
