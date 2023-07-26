const saveDataToLocalStorage = (privateChats) => {
    localStorage.setItem('privateChats', JSON.stringify(Array.from(privateChats.entries())));
  };
  
  const loadDataFromLocalStorage = () => {
    const data = localStorage.getItem('privateChats');
    return data ? new Map(JSON.parse(data)) : new Map();
  };
  
  export { saveDataToLocalStorage, loadDataFromLocalStorage };
  