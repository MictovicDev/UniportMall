const form = document.getElementById('form-data')
const postform = document.querySelectorAll('#post-form')
const newform = document.getElementById('form-like')
const likelist = document.querySelectorAll('.like-button')


postform.forEach(form=>{
  form.addEventListener("submit", (e)=>{
    let id =  e.target.name;
    let text = form.children[1].value;
    let Form = new FormData(form);

    fetch("", {
        method: "POST",
        body: JSON.stringify({"form":Form,"id":id,"text":text}),
    })
    
  })
})


    




function inc_like(id){
       console.log(id)
       likes = document.getElementById(id)
       console.log(likes)
       const mybody = {'id': id}
       fetch('inc-like',{
         method: "POST",
         body: JSON.stringify(mybody)
        
       })
       .then(res=>res.json())
       .then(data=>{
        console.log(data.likes)
        if(data.likes <=1){
          console.log(likes.innerHTML)
          likes.innerHTML = `<i class="far fa-thumbs-up"></i><span class="like-count">${data.likes}</span> Like`
        }
        else{
          likes.innerHTML = `<i class="far fa-thumbs-up"></i><span class="like-count">${data.likes}</span> Likes`
        }

         
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



















// var socket = new WebSocket('ws://localhost:8000/ws/posts/');
// console.log(document.querySelector('#post'))
// const myinterval = setInterval(function updatehtml(event){
//     const  postSection = document.querySelector('#section')

//     fetch('live-post',{
//         method: 'POST',
//         body: JSON.stringify({'page': check()})

//     })
//     .then(res=>res.json())
//     .then(data=>{
//     //var data = JSON.parse(event.data)
//     console.log(data)
//     postSection.innerHTML=''
//     data.forEach(post=>{
//         console.log(data)
//         const a = `<a href="details/${post.id}"></a>`
        
//         const hold = document.createElement('div');
//         const image_container = document.createElement('div')
//         image_container.className='grid-container';
//         hold.id = post.id
//         hold.className = "box box-success";
//         hold.style.marginTop = "30px";
//         hold.style.borderTop = "solid 2px darkgray";
//         hold.style.borderBottom = "solid 2px darkgray";
//         const header = `<h2 id="title"style="padding-left: 20px; margin-bottom: 30px;" class="most_text">${post.title} <br></h2>`
//         hold.insertAdjacentHTML('beforeend', header)
//         const first_p = `<p id="owner" style="padding-left: 20px; padding-bottom: 20px;" class="post_text">Post By : ${post.username}</p>`
//         hold.insertAdjacentHTML('beforeend', first_p)
//         const sec_p =  `<p id="content" style="padding-left: 20px;" class="lorem_text">${post.content}</p> `
//         hold.insertAdjacentHTML('beforeend', sec_p)
//         post.post_image.forEach(image=>{
//             const a = `
//             <div  id="imageuri" class="grid-item">
//                 <a href="${image}"><img src="${image}" alt="image"></a>
//             </div>`
            
//             image_container.insertAdjacentHTML('beforeend',a)
//         })
//         hold.appendChild(image_container)
//         const like = `
//         <div class="button-container">
//             <button onclick="inc_like(${post.id})" id=${post.id} class="like-button"><i class="far fa-thumbs-up"></i><span class="like-count">${post.likes}</span> Like</button>
//             <a href="details/${post.id}"><button onclick="comment(${post.id})" id=${post.id} class="comment-button"><i class="far fa-comment-alt"></i><span class="comment-count">8</span>  Comment</button></a>
//             <a href= "details/${post.id}"><button onclick="details(${post.id})" class="share-button"><i class="fa fa-dashboard"></i>Merchant's Shop</button></a>   
//         </div>
//         <br>
//         `
//         hold.insertAdjacentHTML('beforeend', like)
//         //a.insertAdjacentHTML('beforeend', hold.innerHTML)
//         // postSection.innerHTML = hold.innerHTML
//         //postSection.insertAdjacentHTML('afterbegin', hold.innerHTML)
//         //console.log('added')
//         postSection.innerHTML += hold.outerHTML
//         //postSection.insertAdjacentHTML('beforeend', hold.outerHTML)
//         //console.log(hold)
//     })
// })

// },1000)



function details(id){
    fetch('details/'+ id,{
        method: 'GET'
    })
}




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


                
            



