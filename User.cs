using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoJindan
{
    public partial class User : Form
    {
        public User()
        {
            InitializeComponent();
        }

        private void User_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.FixedSingle;

            schoolSido.Focus();
            LoadData();
        }
        private void LoadData()
        {
            try
            {
                if (!File.Exists("user.txt"))
                {
                    using (File.CreateText("user.txt"))
                    {
                        SaveData();
                    }
                        Close();

                    return;
                }

                string[] datas = File.ReadAllLines("user.txt");

                if (datas.Length == 0)
                    return;

                schoolSido.Text = datas[0].Trim();
                schoolLevel.Text = datas[1].Trim();
                schoolName.Text = datas[2].Trim();

                studentName.Text = datas[3].Trim();
                studentDayOfBirth.Text = datas[4].Trim();
                studentPassword.Text = datas[5].Trim();

                
            }
            catch (Exception e)
            {
                
            }
        }
        

        private void buttonSave_Click(object sender, EventArgs e)
        {
            SaveData();
            Close();
        }
        private void SaveData()
        {
            string data = "";

            data += schoolSido.Text.ToString() + "\n";
            data += schoolLevel.Text.ToString() + "\n";
            data += schoolName.Text + "\n";

            data += studentName.Text + "\n";
            data += studentDayOfBirth.Text + "\n";
            data += studentPassword.Text;

            using (StreamWriter outputFile = new StreamWriter(@"user.txt"))
            {
                outputFile.WriteLine(data);
            }
        }

        private void buttonCancel_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
