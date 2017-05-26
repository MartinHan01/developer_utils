


class ClassData:

    name_list = []
    type_list = []
    id_list = []
    find_list = []
    content_view = ''


    def get_content_view_string(self):
        return str('setContentView(%s);' % self.content_view)

    def get_find_view_string(self):
        find_list = []
        for i in range(len(self.name_list)):
            find_list.append('%s = (%s)findViewById(%s);' \
                            % (self.name_list[i], self.type_list[i], \
                             self.id_list[len(self.id_list) - 1]))

        return find_list


        