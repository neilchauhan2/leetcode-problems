type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
  let filterArr: number[] = [];
    arr.forEach((element, i) => {
      if (fn(element, i)) {
        filterArr.push(element)
      }
    })
    return filterArr;
};