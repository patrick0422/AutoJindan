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
            LoadData();
        }
        private void LoadData()
        {
            try
            {
                string[] datas = System.IO.File.ReadAllLines("user.txt");
                schoolSido.SelectedItem = datas[0].Trim();
                schoolLevel.SelectedItem = datas[1].Trim();
                schoolName.Text = datas[2].Trim();

                studentName.Text = datas[3].Trim();
                studentDayOfBirth.Text = datas[4].Trim();
                studentPassword.Text = datas[5].Trim();
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("user.txt 파일을 찾을 수 없습니다.", "파일을 찾을 수 없음", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Close();
            }
        }

        private void buttonSave_Click(object sender, EventArgs e)
        {
            //TODO
            string data = "";

            data += schoolSido.SelectedItem.ToString() + "\n";
            data += schoolLevel.SelectedItem.ToString() + "\n";
            data += schoolName.Text + "\n";

            data += studentName.Text + "\n";
            data += studentDayOfBirth.Text + "\n";
            data += studentPassword.Text;

            using (StreamWriter outputFile = new StreamWriter(@"user.txt"))
            {
                outputFile.WriteLine(data);
            }

            Close();
        }

        private void buttonCancel_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
