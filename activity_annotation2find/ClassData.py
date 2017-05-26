


class ClassData:

    name_list = []
    type_list = []
    id_list = []
    find_list = []
    content_view = ''
    event_dict = {}

    def get_content_view_string(self):
        return str('setContentView(%s);' % self.content_view)

    def get_find_view_string(self):
        find_list = []
        for i in range(len(self.name_list)):
            find_list.append('%s = (%s)findViewById(%s);' \
                            % (self.name_list[i], self.type_list[i], \
                             self.id_list[len(self.id_list) - 1]))

        return find_list

    def get_set_listener_lines(self, key, space):
        listener_lines = []
        listener_lines.append(space + 'findViewById(%s).setOnClickListener(new View.OnClickListener() {\n' % key)
        listener_lines.append(space + '    @Override\n')
        listener_lines.append(space + '    public void onClick(View v) {\n')
        listener_lines.append(space + '        %s(v);\n' % self.event_dict[key])
        listener_lines.append(space + '    }\n')
        listener_lines.append(space + '});\n')
        return listener_lines
        