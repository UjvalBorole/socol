// SIDEBAR
const menuItems = document.querySelectorAll('.menu-item');

//MESSAGES
const messagesNotification = document.querySelector('#messages-notifications');
const messages = document.querySelector(".messages");
const message = messages.querySelectorAll('.message');
const messageSearch = document.querySelector('#message-search');

//THEME
const theme = document.querySelector('#theme')
const themeModel = document.querySelector('.customize-theme')
const fontsizes = document.querySelectorAll('.choose-size span')
var root = document.querySelector(':root');
const colorPalette = document.querySelectorAll('.choose-color span')
const bg1 = document.querySelector('.bg-1');
const bg2 = document.querySelector('.bg-2');
const bg3 = document.querySelector('.bg-3');


//*****************************SIDEBAR************************* */

//remove active class from all menu items
const changeActiveItem = ()=>{
    menuItems.forEach(item =>{
        item.classList.remove('active');
    })
}


menuItems.forEach(item =>{
    item.addEventListener('click',() => {
        changeActiveItem();
        item.classList.add('active');
        if(item.id != 'notification'){
            document.querySelector('.notification-popup').
            style.display = 'none';
        }else{
            document.querySelector('.notification-popup').
            style.display='block';
            document.querySelector('#notification .notification-count').style.display = 'none';
        }
    })
})


//*****************************MESSAGES************************* */
//search chat

const searchMessage = () => {
    const val = messageSearch.value.toLowerCase();
    console.log(val)
    message.forEach(chat => {
        let name = chat.querySelectorAll('h5').textContent.toLowerCase();
        if(name.indexOf(val) != -1){
            chat.style.display = 'flex';
        }else{
            chat.style.display = 'none';
        }
    })
}


messageSearch.addEventListener('keyup',searchMessage);

// highlight messages card when messages menu item is clicked
messagesNotification.addEventListener('click',() => {
    messages.style.boxShadow = '0 0 1rem var(--color-primary)';
    messagesNotification.querySelector('.notification-count').style.display = 'none';
    setTimeout(()=>{
        messages.style.boxShadow = 'none';
    },2000);

})

// THEME DISPLAY CUSTOMIZATION

//opens model
const openThemeModel = () => {
    themeModel.style.display = 'grid';
}


//cose model
const closeThemeModel = (e) => {
    if(e.target.classList.contains('customize-theme'))

        themeModel.style.display = 'none';
}



themeModel.addEventListener('click',closeThemeModel);
theme.addEventListener('click',openThemeModel);



//*****************************FONTS************************* */
//remove active class for spans or font size selector
const removeSizeSelector = () => {
    fontsizes.forEach(size => {
        size.classList.remove('active');
    })
}
fontsizes.forEach(size => {

    size.addEventListener('click',()=>{
        removeSizeSelector();
        let fontsize;
        size.classList.toggle('active');
        if(size.classList.contains('font-size-1')){
            fontsize = '10px';
            root.style.setProperty('----sticky-top-left','5.4rem');
            root.style.setProperty('----sticky-top-right','5.4rem');
        }else if(size.classList.contains('font-size-2')){
            fontsize = '12.5px';
            root.style.setProperty('----sticky-top-left','5.4rem');
            root.style.setProperty('----sticky-top-right','-7rem');
    
        }else if(size.classList.contains('font-size-3')){
            fontsize = '14.5px';
            root.style.setProperty('----sticky-top-left','-2rem');
            root.style.setProperty('----sticky-top-right','-17rem');
    
        }else if(size.classList.contains('font-size-4')){
            fontsize = '16.5px';
            root.style.setProperty('----sticky-top-left','-5rem');
            root.style.setProperty('----sticky-top-right','-25rem');
        }else if(size.classList.contains('font-size-5')){
            fontsize = '18.5px';
            root.style.setProperty('----sticky-top-left','-12rem');
            root.style.setProperty('----sticky-top-right','-35rem');
    
        }
         //change font size of the root html element
        document.querySelector('html').style.fontSize = fontsize;
    })
 
})

//remove active class from colors
const changeActiveColorClass = () => {
    colorPalette.forEach(colorPicker => {
        colorPicker.classList.remove('active');
    })
}

//change primary colors
colorPalette.forEach(color =>{
    color.addEventListener('click',() => {
        let   primaryHue;
        changeActiveColorClass();
        if(color.classList.contains('color-1')){
            primaryHue = 252;
        }else if(color.classList.contains('color-2')){
            primaryHue = 52;
        }else if(color.classList.contains('color-3')){
            primaryHue = 352;
        }else if(color.classList.contains('color-4')){
            primaryHue =  152;
        }else if(color.classList.contains('color-5')){
            primaryHue = 202;
        }

        color.classList.add('active');
        root.style.setProperty('--primary-color-hue',primaryHue);
    })
})


//theme BACKGROUND values

let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

//changes background color
const changeBG = () =>{
    root.style.setProperty('--dark-color-lightness',darkColorLightness);
    root.style.setProperty('--white-color-lightness',whiteColorLightness);
    root.style.setProperty('--light-color-lightness',lightColorLightness);
}

bg1.addEventListener('click',() => {
  

    //add active class
    bg1.classList.add('active');
    //remove active class from the other
    bg2.classList.remove('active');
    bg3.classList.remove('active');
    
    window.location.reload();
});

bg2.addEventListener('click',() => {
    lightColorLightness = '15%';
    whiteColorLightness = '20%';
    darkColorLightness = '95%';

    //add active class
    bg2.classList.add('active');
    //remove active class from the other
    bg1.classList.remove('active');
    bg3.classList.remove('active');
    changeBG();
})

bg3.addEventListener('click',() => {
    lightColorLightness = '0%';
    whiteColorLightness = '10%';
    darkColorLightness = '95%';

    //add active class
    bg3.classList.add('active');
    //remove active class from the other
    bg1.classList.remove('active');
    bg2.classList.remove('active');
    changeBG();
})


//END