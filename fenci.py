#!/usr/bin/python
# -*- coding: utf-8 -*-
def divide_word(word_list,word,head,max_length):
    won = []
    while (head < len(word)):
        if head + max_length <= len(word):
            flag = head
            for i in range(max_length):
                if word[head:(head+max_length-i)] in word_list:
                    won.append(word[head:(head+max_length-i)])
                    flag = head+max_length-i-1
                    flag1 = head
                    break
            head = flag + 1
        else:
            flag = head
            for i in range(len(word)-head):
                if word[head:(len(word)-i)] in word_list:
                    won.append(word[head:(len(word)-i)])
                    flag = head + len(word)-i
                    flag1 = head
                    break
            head = flag + 1
    return [won,flag1]

if __name__=='__main__':
    #word_list_input = "singer_周杰伦|王力宏|张靓颖|周笔畅;song_月光|青花瓷|天下|笔记|蜀国;actor_周杰伦|张国立|胡歌".decode('utf-8')
    #word_input = "请播放周杰伦的青花瓷".decode('utf-8')
    word_list_input = raw_input().decode("utf-8")
    word_input = raw_input().decode('utf-8')
    entity_list = word_list_input.split(';')
    entity_name_list = []
    entity_value_list = []
    for one_entity in entity_list:
        one_entity_name = one_entity.split('_')[0]
        one_entity_value = one_entity.split('_')[1].split('|')
        entity_name_list.append(one_entity_name)
        entity_value_list.append(one_entity_value)
    word_output_list = []
    output_entity_list = []
    for i in range(len(entity_value_list)):
        won = divide_word(entity_value_list[i], word_input, 0, 10)[0]
        if i == 0:
            headd = divide_word(entity_value_list[i], word_input, 0, 10)[1]
            pre_word = word_input[0:headd]

        if won[0] in word_output_list:
            place =  word_output_list.index(won[0])
            output_entity_list[place] = output_entity_list[place] + [entity_name_list[i]]
        else:
            word_output_list.append(won[0])
            output_entity_list.append( [entity_name_list[i]])
    for i in range(len(output_entity_list)):
        output_entity_list[i].sort()
        output_entity_list[i] =  ','.join(output_entity_list[i])
    output_word = ''
    for i in range(len(word_output_list)):
        output_word = output_word + word_output_list[i] + "\\"+output_entity_list[i]
        if i != len(word_output_list)-1:
            output_word = output_word+ " "
    print pre_word + "." + output_word









