window.onload=function(){
  //실행할 내용
  const code_up_insert_modal    = new bootstrap.Modal(document.getElementById("code_up_insert_modal"))
  const code_up_update_modal    = new bootstrap.Modal(document.getElementById("code_up_update_modal"))
  const code_down_insert_modal  = new bootstrap.Modal(document.getElementById("code_down_insert_modal"))
  
  let before_code = null;
  
  htmx.on("htmx:afterSwap", (e) => { 
    // Response targeting #dialog => show the modal     
    if (e.detail.target.id == "codeDownSwap") {
      // js 요소 접근하기
      let data_target = $(e.detail.target).find('input#code_up_code').attr("datatarget");
      
      if (before_code>0 && data_target == 0) {
        document.getElementById("code_up_"+String(before_code)).click();
      }
      
    }
    // code_up_insert
    if (e.detail.target.id == "code_up_insert_dialog") {
      code_up_insert_modal.show()
    }
    // code_up_update
    if (e.detail.target.id == "code_up_update_dialog"){
      code_up_update_modal.show()
    }
    // code_down_insert
    if (e.detail.target.id == "code_down_insert_dialog") {
      code_down_insert_modal.show()
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "codeDownSwap") {
      // js 요소 접근하기
      let data_target = $(e.detail.target).find('input#code_up_code').attr("datatarget");
      let target_url = "/dev/code_down_list/"+String(data_target);
      $(e.detail.target).attr("hx-get", target_url)
      
      // 비교용 before up code
      before_code = data_target
    }
    //code_up_insert
    if (e.detail.target.id == "code_up_insert_dialog" && !e.detail.xhr.response) {
      code_up_insert_modal.hide()
      e.detail.shouldSwap = false
    }
    // code_up_update
    if (e.detail.target.id == "code_up_update_dialog" && !e.detail.xhr.response) {
      code_up_update_modal.hide()
      e.detail.shouldSwap = false
    }
    //code_down_insert
    if (e.detail.target.id == "code_down_insert_dialog" && !e.detail.xhr.response) {
      code_down_insert_modal.hide()
      e.detail.shouldSwap = false
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("code_up_insert_dialog").innerHTML = ""
  })
}




