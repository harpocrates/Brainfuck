'use strict'

String.prototype.repeat= (n) -> Array(n+1).join(this)

get_sequence = (to, frm=0) ->
  dif = (to-frm) & 255
  if dif > 128 then '-'.repeat(256-dif) else '+'.repeat(dif)

generate_table = () ->
  T = {}
  T[from+' '+to] = get_sequence(to, from) for from in [0...256] for to in [0...256]

  console.log "done first part"

  for from in [0...256]
    for b in [-20..-1].concat([1..20])
      for c in [-20..-1].concat([1..20])
        [a,to] = [from,0]
        for _ in [0...256]
          if a == 0
            competitor = "[#{get_sequence(b)}>#{get_sequence(c)}<]>"
            T[from+' '+to] = competitor if competitor.length < T[from+' '+to].length
            break
          [a,to] = [(a+b) & 255, (to+c) & 255]

  console.log "done second part"

  changes = yes
  loop
    changes = no

    console.log "looping..."

    for from in [0...256]
      for to in [0...256]
        for z in [0...256]
          if T[from+' '+z].length + T[z+' '+to].length < T[from+' '+to].length
            T[from+' '+to] = T[from+' '+z] + T[z+' '+to]
            changes = yes

    break if changes

  console.log "done third part"

  T

generate = (string, T) ->
  [to_parse, to_return] = [ string.charCodeAt(i) for i in [0...string.length] , ""]

  prev = null
  for n in to_parse
    if prev == null
      to_return += T[0+' '+n]+'.'
    else if T[prev+' '+n].length < T[0+' '+n].length+1
      to_return += T[prev+' '+n]+'.'
    else if prev != null
      to_return += '>'+T[0+' '+n]+'.'
    else
      to_return += T[0+' '+n]+'.'
    prev = n

  to_return

exports = {} unless exports?
exports.generate       = generate
exports.generate_table = generate_table