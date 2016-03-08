
/**
  This is to test how javascript can get the elements, feel free to test with this function,
   or comment it out or edit it.
*/


function makeCurrentPriceRequest(barcode, cb){
  qwest.get('/ol6hhqwipb9/inventory/search?barcode=' + barcode.value)
  	.then(function(xhr,resp){
             cb(resp);
         });
}





function calculateMargin(barcode,sellingPrice){

	makeCurrentPriceRequest(barcode,function(resp) {
					    document.getElementById("product").textContent = resp['productName'];
                                            document.getElementById("sell").textContent = sellingPrice.value;
					    var number  = (Number(sellingPrice.value) - Number(resp['currentPrice']))/Number(resp['currentPrice']);
					    document.getElementById("mar").textContent = number;
                                         }
        );

}

function calculateSellingPrice(barcode,margin){
	makeCurrentPriceRequest(barcode,function(resp) {
					    document.getElementById("product").textContent = resp['productName'];
 					    var number  = (Number(margin.value) * Number(resp['currentPrice'])) + Number(resp['currentPrice']);
					    document.getElementById("mar").textContent = margin.value;
                                            document.getElementById("sell").textContent = number;
                                           
                                         }
        );

}







