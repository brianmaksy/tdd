window.Superlists = {};  // a Superlists "namespace" to store initialize function in. 
window.Superlists.initialize = function () { 
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};