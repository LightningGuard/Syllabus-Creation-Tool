
    let currentMonth = 0;
    let selectedDate = null;
    let dueDates = localStorage.getItem('dueDates') ? JSON.parse(localStorage.getItem('dueDates')) : [];

    //will rest the localstorage everytime to empty if you re-access the page for now till there is student accounts
    //that can linked the data they entered to them
    dueDates = [];

    const calendar = document.getElementById('calendar');
    const newAssignment = document.getElementById('newModal');
    const editAssignment = document.getElementById('editModal');
    const modalShow = document.getElementById('modal');
    const userInput = document.getElementById('assignments');
    const userInput2 = document.getElementById('assignments2');
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    function addEvents(date){

        selectedDate = date;

        const assignmentListed = dueDates.find(d => d.date === selectedDate);

        //will check if there is already text within a date that you click and will either prompt you to
        //add an assignment or edit one
        if(assignmentListed){

            newAssignment.style.display = 'block';
            document.getElementById('assignments2').value = assignmentListed.title;
            editAssignment.style.display = 'block';

        }else{

            newAssignment.style.display = 'block';

        }

        modalShow.style.display = 'block';

    }

    function display(){

        const monthDates = new Date();

        //use to traverse the month
        if (currentMonth !== 0){
            monthDates.setMonth(new Date().getMonth() + currentMonth);
        }

        //will get the date of the day
        const day = monthDates.getDate();

        //will get the month
        const month = monthDates.getMonth();

        //will get the year
        const year = monthDates.getFullYear();

        //this will determine how many days are within a month
        const daysWithinMonths = new Date(year, month+1, 0).getDate();

        //will be the first day of the month
        const firstDay = new Date(year, month, 1);

        const dateLayout = firstDay.toLocaleDateString('en-us', {
            weekday: 'long',
            month: 'numeric',
            day: 'numeric',
            year: 'numeric',
        });

        //to determine the days that are not included in that normal month
        const unincludedDays = days.indexOf(dateLayout.split(', ')[0]);

        document.getElementById('showMonth').innerText = `${monthDates.toLocaleDateString('en-us', {month: 'long'})} ${year}` ;

        calendar.innerHTML = '';

        //will create the calendar boxes and determine to show a box for a certain date whether it is included in that month
        for(let i = 1; i <= unincludedDays + daysWithinMonths; i++){
            const boxes = document.createElement('div');
            boxes.classList.add('day');

            if(i > unincludedDays) {

                boxes.innerText = i - unincludedDays;
                const assignmentListed = dueDates.find(d => d.date === `${month + 1}/${i - unincludedDays}/${year}`);

                //will highlight the current day of the current month
                if(i - unincludedDays === day && currentMonth === 0){

                    boxes.id = 'currentDay';

                }

                //will check if there is data to add to the boxes
                if (assignmentListed) {

                    const assignmentDiv = document.createElement('div');
                    assignmentDiv.classList.add('assignmentPrint');
                    assignmentDiv.innerText = assignmentListed.title;
                    boxes.appendChild(assignmentDiv);

                }

                boxes.addEventListener('click', () => addEvents(`${month + 1}/${i - unincludedDays}/${year}`));

            } else {

                boxes.classList.add('dontShow');
            }

            calendar.appendChild(boxes);
        }

    }

    //will enable the buttons to work
    function useButtons(){

        //will be used to go to previous month
        document.getElementById('previousMonth').addEventListener("click", lastMonth)

        //will be used to go to next month
        document.getElementById('nextMonth').addEventListener("click", NextMonth)

        document.getElementById('Add').addEventListener("click", addAssignment)

        document.getElementById('Exit').addEventListener("click", closeWindow)

        document.getElementById('Save').addEventListener("click", editText)

        document.getElementById('Close').addEventListener("click", closeWindow)

    }

    //will let you view a previous month and increment it
    function lastMonth(){

        currentMonth--;
        display();

    }

    //will let you view the next month and increment it
    function NextMonth(){

        currentMonth++;
        display();

    }

    //will close the pop up screen for the user to enter data
    function closeWindow(){

        newAssignment.style.display = 'none';
        editAssignment.style.display = 'none';
        modalShow.style.display = 'none';
        userInput.value = '';
        userInput2.value = '';
        selectedDate = null;
        display();

    }

    //will add the data you entered into localstorage and will be able to show it
    function addAssignment(){

        if (userInput.value){

            dueDates.push({
                date: selectedDate,
                title: userInput.value,
            });

            localStorage.setItem('dueDates', JSON.stringify(dueDates));
        }

        closeWindow();

    }

    //will let you edit the previous data you had and change it or remove it and set the box to empty
    function editText(){

        if (userInput2.value) {

            dueDates = dueDates.filter(e => e.date !== selectedDate);
            localStorage.setItem('dueDates', JSON.stringify(dueDates));

            dueDates.push({
                title: userInput2.value,
                date: selectedDate,
            });

            localStorage.setItem('dueDates', JSON.stringify(dueDates));
        } else{

            dueDates = dueDates.filter(e => e.date !== selectedDate);
            localStorage.setItem('dueDates', JSON.stringify(dueDates));

        }

        closeWindow();

    }

    useButtons();
    display();

