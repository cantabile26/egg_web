window.onload=function(){
  //실행할 내용
  const code_up_insert_modal = new bootstrap.Modal(document.getElementById("code_up_insert_modal"))
  const code_up_update_modal = new bootstrap.Modal(document.getElementById("code_up_update_modal"))
  
  htmx.on("htmx:afterSwap", (e) => { 
    // Response targeting #dialog => show the modal     
    // code_up_insert
    if (e.detail.target.id == "code_up_insert_dialog") {
      code_up_insert_modal.show()
    }
    // code_up_update
    if (e.detail.target.id == "code_up_update_dialog"){
      console.log(e.detail.xhr.response)
      code_up_update_modal.show()
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    //code_up_insert
    if (e.detail.target.id == "code_up_insert_dialog" && !e.detail.xhr.response) {
      console.log(e.detail.xhr.response)
      code_up_insert_modal.hide()
      e.detail.shouldSwap = false
    }
    // code_up_update
    if (e.detail.target.id == "code_up_update_dialog" && !e.detail.xhr.response) {
      code_up_update_modal.hide()
      e.detail.shouldSwap = false
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("code_up_insert_dialog").innerHTML = ""
  })
}