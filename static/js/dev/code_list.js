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


function closeModal() {
  let modal = document.querySelector(".modal");
  modal.style.display = "none"
}

const page_elements = document.getElementsByClassName("page-link");
Array.from(page_elements).forEach(function(element) {
    element.addEventListener('click', function() {
        document.getElementById('page').value = this.dataset.page;
        document.getElementById('searchForm').submit();
    });
});

const btn_search = document.getElementById("btn_search");
btn_search.addEventListener('click', function() {
    document.getElementById('kw').value = document.getElementById('search_kw').value;
    document.getElementById('page').value = 1;  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
    document.getElementById('searchForm').submit();
});