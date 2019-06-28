

function preview(){

    let fileName = document.querySelector('#file').value;
    let lastIndex = fileName.lastIndexOf('.');
    let fileExt = fileName.slice(lastIndex);
    var allowed_types =  ['.jpg', '.png', '.pdf', '.jpeg', '.doc', '.docx','.txt', '.odt', '.odp', '.ods', '.xls', '.xlsx', '.ppt', '.pptx', '.rtf'];
    if  (allowed_types.includes(fileExt)){
        if(fileExt == '.pdf'){
            const file=document.querySelector("#file").files[0];
            let reader = new FileReader();
            reader.addEventListener("load", function (){
                let dt = reader.result;
                previewpdf(dt);
            }, false);
            if (file) {
                reader.readAsDataURL(file);
            }
        }
        else{
            //Converting all file to pdf
            
        }
    }
    else{
        //File Type Not Allowed
    }
}

//Declaring Variables
let pdfDoc,
    pageNum,
    pageIsRendering,
    pageNumIsPending,
    scale,
    canvas,
    ctx;

//Creating And Removing Canvas
let canvasCount = 0;
function getCanvasElement(){
    let container = document.querySelector('#container');
    let canvas = document.createElement("canvas");
    let id;
    if(canvasCount == 0){
        canvasCount++;
    }
    else{
        id = "my-canvas" + canvasCount;
        let removingElement = document.getElementById(id);
        container.removeChild(removingElement);
        canvasCount++;
    }
    id = "my-canvas"+canvasCount;
    canvas.setAttribute("id",id);
    container.appendChild(canvas);
    return(id);
}
//Get document
function previewpdf(data){
    pdfDoc = null,
    pageNum = 1,
    pageIsRendering = false,
    pageNumIsPending = null,
    scale = 1;
    //Getting new canvas id
    let id = getCanvasElement();
    canvas = document.getElementById(id),
    ctx = canvas.getContext('2d');

    pdfAsArray = convertDataURIToBinary(data)
    pdfjsLib.getDocument(pdfAsArray).promise.then(pdfDoc_=>{
        pdfDoc = pdfDoc_;
    
        document.querySelector('#page-count').textContent = pdfDoc.numPages;

        renderPage(pageNum);
    });

}

//for converting base64 to arrayunit8
function convertDataURIToBinary(dataURI){
    let BASE64_MARKER = ';base64,';
    let base64Index = dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
    let base64 = dataURI.substring(base64Index);
    let raw = window.atob(base64);
    let rawLength = raw.length;
    let array = new Uint8Array(new ArrayBuffer(rawLength));

    for(let i = 0; i < rawLength; i++) {
        array[i] = raw.charCodeAt(i);
    }
    return array;
}

//Render the page
const renderPage = num => {
    pageIsRendering = true;

    //Get Page
    pdfDoc.getPage(num).then(page =>{
        //Set Scale
        document.querySelector("#previewmodal").style.display = "block";
        let container = document.querySelector('#container');
        let viewport = page.getViewport(1);
        scale = container.clientWidth / viewport.width;
        viewport = page.getViewport(scale);
        canvas.height =  viewport.height;
        canvas.width = viewport.width;

        const renderCtx = {
            canvasContext: ctx,
            viewport
        }
        page.render(renderCtx).promise.then(() =>{
            pageIsRendering = false;

            if(pageNumIsPending !== null){
                renderPage(pageNumIsPending);
                pageNumIsPending = null;
            }
        });

        //Output Current Page
        document.querySelector('#page-num').textContent = num;  
    });
    
};

// Check for pages rendering
const queueRenderPage = num =>{
    if(pageIsRendering){
        pageNumIsPending = num;
    }else{
        renderPage(num);
    }
}

//Show Prev Page
const showPrevPage = () => {
    if(pageNum <= 1){
        return;
    }
    pageNum--;
    queueRenderPage(pageNum);
}

//Show Next Page
const showNextPage = () => {
    if(pageNum >= pdfDoc.numPages){
        return;
    }
    pageNum++;
    queueRenderPage(pageNum);
}


//Button Events
document.querySelector('#prev').addEventListener('click',showPrevPage);
document.querySelector('#next').addEventListener('click',showNextPage);
