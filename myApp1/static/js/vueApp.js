const API_URL = 'http://192.168.1.8:5005'


var app = new Vue(
    {
        el: "#app",
        delimiters: ["[[","]]"],
        data: function () {
            console.log("I am inside DATA")
            return {
                title: "Notemaster!",
                isLoading: false,
                note: {
                    text: ""
                },
                notes: [
                        {id: 1, text: "test note 1", date: "20180705_16h04m05s"}, 
                        {id: 3, text: "Note format string test for status", date: "20180705_16h05m54s"}
                ]
            }
        },
        methods: {
            addNote() {
                let { text } = this.note
                this.notes.push(
                    { id: 111, text, date: new Date(Date.now()).toLocaleString() }
                )
                this.postNote(this.note.text)
                this.getAllNotes()
            },
            
            postNote(arg1) {
                console.log("I am inside PostNote axios JS function!")
                console.log("This is the API URL: " + API_URL)
                axios.post(`${API_URL}/postNote`, {
                    text: arg1
                })
                    .then(function (response) {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        },

        created() {
            // https://stackoverflow.com/questions/40996344/axios-cant-set-data
            console.log("I've started in created")
            axios.get(`${API_URL}/getAllNotes`)
                .then((response) => {
                    this.notes = response.data.map(JSON.parse);
                }).catch(function (error) {
                    console.log("I am in error")
                    // handle error
                    console.log(error);
                })
                .then(function () {
                    console.log("I am finally here")
                    // always executed
                });
        }
    }
) 