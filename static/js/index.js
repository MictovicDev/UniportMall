const form = document.getElementById('form-data')
const newform = document.getElementById('form-like')
const likelist = document.querySelectorAll('.like-button')
//console.log(likelist)



function inc_like(id){
       mybody = {'id': id}
       fetch('inc-like',{
         body: JSON.stringify(mybody),
         method: "POST",
       })
}



form.addEventListener("submit", (e)=>{
    e.preventDefault()
    const formData = new FormData(form)
    console.log('submitted')
    
    fetch("ajax-post", {
        body: formData,
        method: "POST",
    })

})



function comment(id) {
    const commentForm = document.querySelectorAll('.comment-form')
    commentForm.forEach(my_data=>{
        console.log(my_data)
        if(my_data.getAttribute('data-form-id') == id){
            if(my_data.classList.contains("is-open")){
                my_data.classList.remove("is-open");
            }
            else{
                my_data.classList.add("is-open");
            }
        }
})}

// const data = [1,2,3]

// var my_cover = document.querySelectorAll('#cover')
// console.log(my_cover[0].remove())
// var my_cover = document.querySelectorAll('#cover')
// console.log(my_cover)


// if(data.length != 4){
//     for(i=0; i< 4-data.length; i++){
//         my_cover[my_cover.length-1].remove()
//         var my_cover = document.querySelectorAll('#cover')
//         console.log(my_cover)
//     }
// }











// var socket = new WebSocket('ws://localhost:8000/ws/posts/');
console.log(document.querySelector('#post'))
const myinterval = setInterval(function updatehtml(event){
    const  postSection = document.querySelector('#section')

    fetch('live-post',{
        method: 'POST',
        body: JSON.stringify({'page': check()})

    })
    .then(res=>res.json())
    .then(data=>{
    //var data = JSON.parse(event.data)
    console.log(data)
    postSection.innerHTML=''
    data.forEach(post=>{
        console.log(data)
        const a = `<a href="details/${post.id}"></a>`
        
        const hold = document.createElement('div');
        const image_container = document.createElement('div')
        image_container.className='grid-container';
        hold.id = post.id
        hold.className = "box box-success";
        hold.style.marginTop = "30px";
        hold.style.borderTop = "solid 2px darkgray";
        hold.style.borderBottom = "solid 2px darkgray";
        const header = `<h2 id="title"style="padding-left: 20px; margin-bottom: 30px;" class="most_text">${post.title} <br></h2>`
        hold.insertAdjacentHTML('beforeend', header)
        const first_p = `<p id="owner" style="padding-left: 20px; padding-bottom: 20px;" class="post_text">Post By : ${post.username}</p>`
        hold.insertAdjacentHTML('beforeend', first_p)
        const sec_p =  `<p id="content" style="padding-left: 20px;" class="lorem_text">${post.content}</p> `
        hold.insertAdjacentHTML('beforeend', sec_p)
        post.post_image.forEach(image=>{
            const a = `
            <div  id="imageuri" class="grid-item">
                <a href="${image}"><img src="${image}" alt="image"></a>
            </div>`
            
            image_container.insertAdjacentHTML('beforeend',a)
        })
        hold.appendChild(image_container)
        const like = `
        <div class="button-container">
            <button onclick="inc_like(${post.id})" id=${post.id} class="like-button"><i class="far fa-thumbs-up"></i><span class="like-count">${post.likes}</span> Like</button>
            <a href="details/${post.id}"><button onclick="comment(${post.id})" id=${post.id} class="comment-button"><i class="far fa-comment-alt"></i><span class="comment-count">8</span>  Comment</button></a>
            <a href= "details/${post.id}"><button onclick="details(${post.id})" class="share-button"><i class="fa fa-dashboard"></i>Merchant's Shop</button></a>   
        </div>
        <br>
        `
        hold.insertAdjacentHTML('beforeend', like)
        //a.insertAdjacentHTML('beforeend', hold.innerHTML)
        // postSection.innerHTML = hold.innerHTML
        //postSection.insertAdjacentHTML('afterbegin', hold.innerHTML)
        //console.log('added')
        postSection.innerHTML += hold.outerHTML
        //postSection.insertAdjacentHTML('beforeend', hold.outerHTML)
        //console.log(hold)
    })
})

},1000)



function details(id){
    fetch('details/'+ id,{
        method: 'GET'
    })
}

const previous = document.querySelector('#previous')
const next = document.querySelector('#next')
function check(){
    next.addEventListener("click", function(e){
    return next.textContent
})}


const hamburer = document.querySelector(".hamburger");
const navList = document.querySelector(".nav-list");

if (hamburer) {
  hamburer.addEventListener("click", () => {
    navList.classList.toggle("open");
  });
}

// Popup
const popup = document.querySelector(".popup");
const closePopup = document.querySelector(".popup-close");

if (popup) {
  closePopup.addEventListener("click", () => {
    popup.classList.add("hide-popup");
  });

  window.addEventListener("load", () => {
    setTimeout(() => {
      popup.classList.remove("hide-popup");
    }, 1000);
  });
}


// var my_cover = document.querySelectorAll('#cover');
// let my = [1,2]
// console.log(4-my.length)
//const length = 4-my.length
// if(my.length != 4){
//     const Length = 4-my.length
//     console.log(Length)
//     for(i=0; i<Length; i++){
//         my_cover[my_cover.length-1].remove()
//         var my_cover = document.querySelectorAll('#cover')
//         console.log(my_cover)
//     }
// }


//likes[i].children[0].textContent = `${mydata[i].likes} Like`
// likes[i].children[1].textContent = `${data[i].comments} Comment`



//console.log(previous)





// previous.addEventListener("click", function(e){
//     //e.preventDefault()
    
//     fetch('pagination',{
//         method: 'POST',
//         body: JSON.stringify({'page': previous.textContent})
//     })
//     .then(res=>res.json())
//     .then(data=>{
//         console.log(data)
//     })
// })

// next.addEventListener("click", function(e){
//     document.documentElement.scrollTop = 0;
//     fetch('live-post',{
//         method: 'POST',
//         body: JSON.stringify({'page': next.textContent})
//     })
//     .then(res=>res.json())
//     .then(data=>{
//         // console.log(data)
//         // var my_cover = document.querySelectorAll('#cover')
//         // if(data.length != 4){
//         //     for(i=0; i< 4-data.length; i++);{
//         //         my_cover[my_cover.length-1].outerHTML = ''
//         //         my_cover[my_cover.length-1].remove()
//         //         var my_cover = document.querySelectorAll('#cover')  
//         //     }
//         // }
//         //const post = document.querySelectorAll('#post')
//        //console.log(data)
//     //    for(let i=0; i<my_cover.length; i++){
//     //        const image_container = document.createElement('div')
//     //        image_container.className='grid-container';
//     //        my_cover[i].innerHTML = ''
//     //        //console.log(data[i])
//     //        //console.log(my_cover[i])
//     //        const hold = document.createElement('div')
//     //        const title = `<h2 id="title" style="padding-left: 20px; margin-bottom: 30px;"class="most_text">${data[i].title}</h2>`
//     //        hold.innerHTML += title
//     //        const user = `<p id="owner"  style="padding-left: 20px; padding-bottom: 20px;"class="post_text">Post By : ${data[i].username}</p>`
//     //        hold.innerHTML += user
//     //        const content = `<p id="content" type="content" style="padding-left: 20px;" class="lorem_text">${data[i].content}</p>`
//     //        hold.innerHTML += content
//     //        data[i].post_image.forEach(image=>{
//     //            const img = `<div  id="imageuri" class="grid-item">
//     //                                        <a href="${image}"><img src="${image}" alt="image"></a>
//     //                        </div>`
//     //            image_container.insertAdjacentHTML('beforeend',img)
//     //        })
//     //        hold.appendChild(image_container)
//     //        my_cover[i].insertAdjacentHTML('beforeend', hold.outerHTML)
//     //        //console.log(my_cover)
//     //    }
//     })
  
// })


                
            



