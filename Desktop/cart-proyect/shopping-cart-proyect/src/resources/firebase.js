// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCPuT54twbVZ8BBj_4Vz2QXXIrFycm091U",
    authDomain: "shopping-cart-proyect-9836b.firebaseapp.com",
    projectId: "shopping-cart-proyect-9836b",
    storageBucket: "shopping-cart-proyect-9836b.appspot.com",
    messagingSenderId: "345494553042",
    appId: "1:345494553042:web:3011c5b5963e60d1f5080b",
    measurementId: "G-79JY80PHBQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);