import os
import glob
import re

replacements = {
    "Voluptatem dignissimos provident laboris nisi ut aliquip ex ea commodo": "Empowering teams with seamless collaboration and productivity tools",
    "Ut fugiat ut sunt quia veniam. Voluptate perferendis perspiciatis quod nisi et. Placeat debitis quia recusandae odit et consequatur voluptatem. Dignissimos pariatur consectetur fugiat voluptas ea.": "Discover a new way to manage your workflows. Our platform brings together all the essential tools you need to streamline operations and drive business growth. Experience unparalleled efficiency and intuitive design.",
    "Temporibus nihil enim deserunt sed ea. Provident sit expedita aut cupiditate nihil vitae quo officia vel. Blanditiis eligendi possimus et in cum. Quidem eos ut sint rem veniam qui. Ut ut repellendus nobis tempore doloribus debitis explicabo similique sit. Accusantium sed ut omnis beatae neque deleniti repellendus.": "Stay ahead of the curve with our innovative solutions. We provide comprehensive analytics, robust security, and seamless integrations. Whether you are a startup or an enterprise, our platform scales with your needs. Unlock your full potential and achieve your goals with confidence.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.": "Experience the future of SaaS platforms, designed to optimize performance and elevate your business strategies to new heights.",
    "Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate trideta storacalaperda mastiro dolore eu fugiat nulla pariatur.": "Leverage automated workflows to minimize manual tasks and focus on what truly matters for your company's success.",
    "Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident": "Join thousands of satisfied customers who have revolutionized their daily operations. Our dedicated support team ensures you are always up and running.",
    "Ullamco laboris nisi ut aliquip ex ea commodo consequat.": "Streamline your processes and boost team productivity.",
    "Duis aute irure dolor in reprehenderit in voluptate velit.": "Gain actionable insights with our advanced analytics.",
    "Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum": "Join thousands of satisfied customers who have revolutionized their daily operations. Our dedicated support team ensures you are always up and running. Maximize your potential today.",
    "Nesciunt Mete": "Cloud Storage",
    "Provident nihil minus qui consequatur non omnis maiores. Eos accusantium minus dolores iure perferendis.": "Secure, scalable, and reliable cloud storage solutions tailored for your business needs.",
    "Eosle Commodi": "Data Analytics",
    "Ut autem aut autem non a. Sint sint sit facilis nam iusto sint. Libero corrupti neque eum hic non ut nesciunt dolorem.": "Transform raw data into meaningful insights with our powerful and intuitive analytics engine.",
    "Ledo Markt": "Team Collaboration",
    "Ut excepturi voluptatem nisi sed. Quidem fuga consequatur. Minus ea aut. Vel qui id voluptas adipisci eos earum corrupti.": "Enhance communication and collaboration within your team through real-time messaging and file sharing.",
    "Modi sit est dela pireda nest": "Advanced Data Security",
    "Unde praesenti mara setra le": "Seamless API Integration",
    "Pariatur explica nitro dela": "Customizable Dashboards",
    "Nostrum qui dile node": "24/7 Premium Support",
    "Voluptatem dignissimos provident quasi corporis voluptates sit assumenda.": "Comprehensive tools designed for modern digital workflows.",
    "Neque exercitationem debitis soluta quos debitis quo mollitia officia est": "Accelerate your growth with data-driven decision making.",
    "Voluptatibus commodi ut accusamus ea repudiandae ut autem dolor ut assumenda": "Scale your infrastructure effortlessly as your business expands.",
    "Omnis fugiat ea explicabo sunt dolorum asperiores sequi inventore rerum": "Maintain compliance and ensure top-tier reliability everywhere.",
    "Provident mollitia neque rerum asperiores dolores quos qui a. Ipsum neque dolor voluptate nisi sed.": "Implement state-of-the-art security measures to protect your most valuable assets.",
    "Lorem Ipsum": "Core Infrastructure",
    "Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident": "Build your applications on a solid foundation of robust and high-performance core infrastructure.",
    "Dolor Sitema": "Automated Workflows",
    "Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata": "Reduce manual effort and increase efficiency by automating your repetitive and time-consuming workflows.",
    "Sed ut perspiciatis": "Real-time Monitoring",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur": "Keep track of your system's health and performance with our comprehensive real-time monitoring tools.",
    "Magni Dolores": "Smart Notifications",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum": "Stay informed with intelligent alerts that notify you of critical events and system changes instantly.",
    "Nemo Enim": "Global Reach",
    "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque": "Expand your business globally with our highly distributed architecture and low-latency network.",
    "Eiusmod Tempor": "Flexible Pricing",
    "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi": "Choose from a variety of flexible pricing plans that adapt to your specific business requirements and budget.",
    "Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.": "This platform completely transformed how we handle our internal processes. The intuitive interface and powerful features are a game-changer for our productivity.",
    "Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.": "I've tried many different tools, but nothing comes close to the versatility and reliability offered here. Highly recommended for any growing team.",
    "Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.": "Our sales have increased by 30% since we integrated this SaaS solution. The analytics provided are simply phenomenal and incredibly easy to understand.",
    "Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.": "The customer support team is outstanding. They are always available to help and have resolved any issues we faced within minutes. Truly exceptional service.",
    "Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.": "A robust and scalable platform that easily accommodated our rapid growth. We couldn't have asked for a better partner in our digital transformation journey.",
    "Esse dolorum voluptatum ullam est sint nemo et est ipsa porro placeat quibusdam quia assumenda numquam molestias.": "Discover everything you need to start building your next great application with our comprehensive and easy-to-use template.",
    "Autem ipsum nam porro corporis rerum. Quis eos dolorem eos itaque inventore commodi labore quia quia. Exercitationem repudiandae officiis neque suscipit non officia eaque itaque enim. Voluptatem officia accusantium nesciunt est omnis tempora consectetur dignissimos. Sequi nulla at esse enim cum deserunt eius.": "Our comprehensive approach ensures that every detail of your project is meticulously managed and optimized for success. We focus on delivering robust and scalable solutions that drive measurable results for your business. From initial planning to final execution, our team is dedicated to exceeding your expectations and fostering long-term growth.",
    "Enim qui eos rerum in delectus": "Driving Innovation Through Technology",
    "Aliquam est incidunt. Aliquid nam vel corrupti quo dolorem aut doloremque. Ad sit at voluptatem ea in suscipit qui eum voluptas. Qui ipsam hic amet.": "We leverage the latest technological advancements to deliver innovative solutions that propel your business forward. Our focus is on continuous improvement and staying ahead of industry trends.",
    "Aut quo ipsum dolorum necessitatibus reiciendis aut iusto ut eius.": "Implementing cutting-edge features to streamline operations.",
    "Exercitationem repudiandae officiis neque suscipit": "Delivering Excellence in Every Project",
    "Est voluptatem labore ipsum dolor": "Delivering Quality Solutions",
    "Eximi tempore consequatur magnam non aut accusantium laboriosam": "Building scalable platforms that empower modern businesses.",
    "Ipsa perferendis magnam assumenda nam eum": "Leveraging data to create insightful and actionable metrics."
}

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        pattern = '\\s+'.join(re.escape(word) for word in old.split())
        content = re.sub(pattern, new, content)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob('*.html'):
    process_file(html_file)
