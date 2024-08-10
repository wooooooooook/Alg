function solution(participant, completion) {
  let map = new Map()

  for (let name of participant) {
    if (map.has(name)) {
      map.set(name, map.get(name) + 1)
    } else {
      map.set(name, 1)
    }
  }
  // console.log(map)

  for (let name of completion) {
    map.set(name, map.get(name) - 1)
    if (map.get(name) === 0) {
      map.delete(name)
    }
  }
  // console.log(map)

  for (const key of map.keys())
    return key;
}

// console.assert(solution(["leo", "kiki", "eden"], ["eden", "kiki"]) === "leo", "틀렸습니다.")
// console.assert(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) === "vinko", "틀렸습니다.")
// console.assert(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) === "mislav", "틀렸습니다.")
