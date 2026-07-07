local mapping = {
    ['q']='й', ['w']='ц', ['e']='у', ['r']='к', ['t']='е', ['y']='н', ['u']='г', ['i']='ш', ['o']='щ', ['p']='з', ['[']='х', [']']='ъ',
    ['a']='ф', ['s']='ы', ['d']='в', ['f']='а', ['g']='п', ['h']='р', ['j']='о', ['k']='л', ['l']='д', [';']='ж', ["'"]='э',
    ['z']='я', ['x']='ч', ['c']='с', ['v']='м', ['b']='и', ['n']='т', ['m']='ь', [',']='б', ['.']='ю', ['`']='ё'
}

local function translate(input, seg)
    local result = ""
    for i = 1, #input do
        local c = input:sub(i,i)
        if mapping[c] then
            result = result .. mapping[c]
        else
            result = result .. c
        end
    end
    
    local cand = Candidate("ru_literal", seg.start, seg._end, result, "")
    -- Give literal transliteration a very low weight so auto-completion takes precedence
    cand.quality = -1
    yield(cand)
end

return translate