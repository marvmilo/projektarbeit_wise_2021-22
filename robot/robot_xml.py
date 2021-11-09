from lxml import etree as ET

class RobotData:
    def set_btp_position(self, pX, pY, pZ, pA, pB, pC):
        accept = (type(0), type(0.0))
        not_accepted_value = 0
        if not type(pX) in accept:
            pX = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pX", pX, not_accepted_value, type(pX)))
        if not type(pY) in accept:
            pY = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pY", pY, not_accepted_value, type(pY)))
        if not type(pZ) in accept:
            pZ = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pZ", pZ, not_accepted_value, type(pZ)))
        if not type(pA) in accept:
            pA = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pA", pA, not_accepted_value, type(pA)))
        if not type(pB) in accept:
            pB = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pB", pB, not_accepted_value, type(pB)))
        if not type(pC) in accept:
            pC = not_accepted_value
            print("Wasn't able to set \"btp_position/{}\" to your Input \"{}\"\nIt's been set to the standard Value \"{}\".\nValue must be a float or integer, the type of your variable is {}!".format("pC", pC, not_accepted_value, type(pC)))
        self.btp_position = {"X": str(pX), "Y": str(pY), "Z": str(pZ), "A": str(pA), "B": str(pB), "C": str(pC)}
    def set_btp_container(self, cnum):
        try:
            self.btp_containernum = str(int(cnum))
        except:
            print("Wasn't able to set \"btp_containernum\" to \"{}\"\nValue must be an integer, the type of your variable is {}!".format(cnum, type(cnum)))
    def set_movementclear(self, mvalue):
        try:
            self.movementclearance = str(int(mvalue))
        except:
            print("Wasn't able to set \"moevementclear\" to \"{}\"\nValue must be an boolean or integer, the type of your variable is {}!".format(mvalue, type(mvalue)))
    
    def create_xml(self, pp=0):
        xml_recv = ET.Element("recv")
        if "movementclearance" in dir(self):
            xml_recv_robot = ET.SubElement(xml_recv, "robot")
            xml_recv_robot_movementclear = ET.SubElement(xml_recv_robot, "movementclear")
            xml_recv_robot_movementclear.text = self.movementclearance
        if "btp_position" in dir(self) and "btp_containernum" in dir(self):
            xml_btp = ET.SubElement(xml_recv, "btp")
            xml_btp_position = ET.SubElement(xml_btp, "position", attrib=self.btp_position)
            xml_btp_containernum = ET.SubElement(xml_btp, "containernum")
            xml_btp_containernum.text = self.btp_containernum
        ret_str = ET.tostring(xml_recv, pretty_print=pp).decode()
        try:
            del self.btp_position, self.movementclearance, self.btp_containernum
        except:
            pass
        return ret_str
    def read_xml(self, xml_data):
        # returns dictionary
        ret_dict = {}
        xml_tree = ET.fromstring(xml_data)
        for xml_snd in xml_tree:
            if xml_snd.tag == "robot":
                for xml_snd_robot in xml_snd:
                    if xml_snd_robot.tag == "position":
                        ret_dict["robot_position"] = "feature not implemented yet(robot_xml.py, line 62)"
                    if xml_snd_robot.tag == "status":
                        ret_dict["robot_status"] = xml_snd_robot.text
            if xml_snd.tag == "btp":
                for xml_snd_btp in xml_snd:
                    if xml_snd_btp.tag == "isplaced":
                        try:
                            ret_dict["btp_isplaced"] = bool(int(xml_snd_btp.text))
                        except:
                            pass
        return ret_dict