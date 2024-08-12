function solution(clothes) {
  // console.log(clothes)
  let answer = 1

  const newClothesList = clothes.map(item => item[1])
  // console.log(newClothesList)

  let map = new Map()
  for (let i of newClothesList) {
    if (map.has(i)) {
      map.set(i, map.get(i) + 1)
    } else {
      map.set(i, 1)
    }
  }
  // console.log(map)

  for (let i of map.values()) {
    answer *= i + 1
  }
  return answer - 1
}

// return 5
// console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
// return 3
// console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
