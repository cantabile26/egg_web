function companyNumEvent(target){
  const cleanInput = $(target).val().replaceAll(/[^0-9]/g, "");
  let result = "";
  const length = cleanInput.length;
  if(length<= 10){
      result = cleanInput;
  }else{
      result = cleanInput.substr(0,10)
  } 
  result = result.replace(/[^0-9]/g, '').replace(/(\d{2})(\d{3})(\d{5})/, '$1-$2-$3');
  $(target).val(result)
}

function telNumEvent(target){
  const cleanInput = $(target).val().replaceAll(/[^0-9]/g, "");
  let result = "";
  const length = cleanInput.length;

  if(length === 8) {
      result = cleanInput.replace(/(\d{4})(\d{4})/, '$1-$2');
  } else if(length === 9 || length === 10) {
      result = cleanInput.replace(/(\d{2})(\d{3,4})(\d{4})/, '$1-$2-$3');
  } else if(length === 10 || length === 11) {
      result = cleanInput.replace(/(\d{3})(\d{3,4})(\d{4})/, '$1-$2-$3');
  } else if(length > 11){
      result = cleanInput.substr(0,11).replace(/(\d{3})(\d{3,4})(\d{4})/, '$1-$2-$3');
  } else {
      result = cleanInput
  }
  $(target).val(result)
}