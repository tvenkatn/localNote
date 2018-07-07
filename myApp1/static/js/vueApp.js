const API_URL = 'http://192.168.1.8:5005'
// const API_URL = 'http://localhost:5005'


var app = new Vue(
    {
        el: "#app",
        delimiters: ["[[","]]"],
        data: function () {
            return {
                title: "local Note",
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
            },
            
            postNote(arg1) {
                axios.post(`${API_URL}/postNote`, {
                    text: arg1
                })
                    .then(function (response) {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },

            removeNote(note) {
                // console.log(note.id);
                this.notes.pop(note); // delete from UI
                axios.delete(`${API_URL}/deleteNote`, { data: { id: note.id } })
                    .then((response) => {
                        // console.log(response)
                    }, (error) => {
                        // error callback
                    });
            }
        },

        created() {
            // https://stackoverflow.com/questions/40996344/axios-cant-set-data
            axios.get(`${API_URL}/getAllNotes`)
                .then((response) => {
                    this.notes = response.data.map(JSON.parse);
                }).catch(function (error) {
                    // handle error
                    console.log(error);
                })
                .then(function () {
                    // always executed
                });
        }
    }
) 
